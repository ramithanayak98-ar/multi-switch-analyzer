"""
Test Validation Suite - 7 Tests
Run AFTER starting POX and Mininet
"""
import subprocess
import time

def run_test(name, cmd, expect_pass=True):
    print(f"\nRunning: {name}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
    output = result.stdout + result.stderr
    print(output[:300])
    return output

print("=" * 50)
print("Multi-Switch Flow Table Analyzer - Validation Tests")
print("=" * 50)

print("\nT1: Check s1 flow table")
run_test("T1 - s1 flows", "sudo ovs-ofctl dump-flows s1")

print("\nT2: Check s2 flow table")
run_test("T2 - s2 flows", "sudo ovs-ofctl dump-flows s2")

print("\nT3: Check s3 flow table")
run_test("T3 - s3 flows", "sudo ovs-ofctl dump-flows s3")

print("\nT4: Check switch connections")
run_test("T4 - switches", "sudo ovs-vsctl show")

print("\nT5: Check OVS version")
run_test("T5 - OVS version", "ovs-vsctl --version")

print("\nT6: Check controller connection")
run_test("T6 - controller", "sudo ovs-ofctl show s1")

print("\nT7: Check all switch ports")
run_test("T7 - ports", "sudo ovs-ofctl dump-ports s1")

print("\n" + "=" * 50)
print("All 7 tests completed!")
print("=" * 50)
