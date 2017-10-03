#ifndef TESTER_HPP
#define TESTER_HPP

#include <iostream>
#include <thread>
#include <atomic>
#include <chrono>

#include <cstring>

#include "hwloc_cpp_helper.hpp"

template<class T>
class tester {
public:
  using meta_data_t = T;

  tester(hwloc_topology_t topo, bitmap_wrapper_t local_node_set,
         bitmap_wrapper_t remote_node_set, size_t memory_size)
      : topo_(topo),
        local_node_set_(move(local_node_set)),
        remote_node_set_(move(remote_node_set)),
        memory_size_(memory_size),
        local_data_(nullptr, hwloc_mem_disposer(topo, memory_size)),
        remote_data_(nullptr, hwloc_mem_disposer(topo, memory_size)),
        running_(new std::atomic<bool>(true)),
        measuring_(new std::atomic<bool>(false)),
        copy_rate_(0) {
    init();
  }

  tester() = delete;
  tester(tester&&) = default;
  tester& operator=(tester&&) = default;
  tester(const tester&) = delete;
  tester& operator=(const tester&) = delete;

  void start_tester() {
    // ATTENTION!! after executing this function, tester cannot be coppied
    // anymore
    thread_ = std::thread(&tester::run_measurement, this);
  }

  void stop_tester() {
    if (thread_.joinable()) {
      thread_.join();
    }
  }

  void start_measurement() {
    measuring_->store(true);
  }

  void stop_measurement() {
    measuring_->store(false);
    running_->store(false);
  }

  // in bytes per seconds
  size_t get_copy_rate() {
    return copy_rate_;
  }

  meta_data_t meta_data;
private:
  void init() {
    auto current_cpu_binding = hwloc_bitmap_make_wrapper();
    hwloc_get_cpubind (topo_, current_cpu_binding.get(), 0),
    pin_this_thread(local_node_set_);
    local_data_.reset(malloc(memory_size_));
    pin_this_thread(remote_node_set_);
    remote_data_.reset(malloc(memory_size_));
    pin_this_thread(current_cpu_binding);

    //remote_data_.reset(hwloc_alloc_membind_nodeset(
      //topo_, memory_size_, remote_node_set_.get(), HWLOC_MEMBIND_BIND,
      //HWLOC_MEMBIND_THREAD | HWLOC_MEMBIND_STRICT));
    //if (remote_data_.get() == nullptr) {
      //std::cerr << "hwloc_alloc_membind_nodeset() for remote memory failed"
                //<< std::endl;
      //exit(EXIT_FAILURE);
    //}
    //local_data_.reset(hwloc_alloc_membind_nodeset(
      //topo_, memory_size_, local_node_set_.get(), HWLOC_MEMBIND_BIND,
      //HWLOC_MEMBIND_THREAD | HWLOC_MEMBIND_STRICT));
    //if (local_data_.get() == nullptr) {
      //std::cerr << "hwloc_alloc_membind_nodeset() for local memory failed"
                //<< std::endl;
      //exit(EXIT_FAILURE);
    //}
  }

  void pin_this_thread(bitmap_wrapper_t& to) {
    auto bind_cpu_set = hwloc_bitmap_make_wrapper();
    hwloc_cpuset_from_nodeset(topo_, bind_cpu_set.get(), to.get());
    auto err =
      hwloc_set_cpubind(topo_, bind_cpu_set.get(),
                        HWLOC_CPUBIND_THREAD | HWLOC_CPUBIND_NOMEMBIND);
    if (err == -1) {
      std::cerr << "hwloc_set_cpubind() failed" << std::endl;
      exit(EXIT_FAILURE);
    }
  }

  void run_measurement() {
    using namespace std::chrono;
    pin_this_thread(local_node_set_);
    while (running_->load() && !measuring_->load()) {
    }
    if (measuring_->load()) {
      auto start = std::chrono::high_resolution_clock::now();
      size_t iterations = 0;
      while (running_->load()) {
        memcpy(local_data_.get(), remote_data_.get(), memory_size_);
        ++iterations;
      }
      auto end = high_resolution_clock::now();
      duration<double> diff = end - start;
      copy_rate_ = (memory_size_ * iterations) / diff.count();
    }
  }

  hwloc_topology_t topo_;
  bitmap_wrapper_t local_node_set_;
  bitmap_wrapper_t remote_node_set_;
  size_t memory_size_; // in bytes
  std::unique_ptr<void, hwloc_mem_disposer> local_data_;
  std::unique_ptr<void, hwloc_mem_disposer> remote_data_;
  std::unique_ptr<std::atomic<bool>> running_;
  std::unique_ptr<std::atomic<bool>> measuring_;
  std::thread thread_;
  size_t copy_rate_; //bytes per seconds
};


#endif // TESTER_HPP
