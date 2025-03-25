# Python's ipaddress Module: How To Guide

# Python의 ipaddress 모듈: 사용 가이드

## Introduction

The `ipaddress` module in Python provides classes and functions for working with IPv4 and IPv6 addresses and networks. Introduced in Python 3.3, this module simplifies IP address manipulation, validation, and network calculations, which are common tasks in network programming, system administration, and cybersecurity.

This guide demonstrates how to use the `ipaddress` module effectively for various IP addressing tasks.

## 소개

Python의 `ipaddress` 모듈은 IPv4 및 IPv6 주소와 네트워크를 다루기 위한 클래스와 함수를 제공합니다. Python 3.3에 도입된 이 모듈은 네트워크 프로그래밍, 시스템 관리 및 사이버 보안에서 흔히 수행하는 작업인 IP 주소 조작, 유효성 검사 및 네트워크 계산을 단순화합니다.

이 가이드는 다양한 IP 주소 지정 작업에 `ipaddress` 모듈을 효과적으로 사용하는 방법을 보여줍니다.

## Basic Concepts

The `ipaddress` module provides three main classes:

1. `IPv4Address` and `IPv6Address`: Represent individual IP addresses
2. `IPv4Network` and `IPv6Network`: Represent IP networks (with subnet masks)
3. `IPv4Interface` and `IPv6Interface`: Represent IP interfaces (addresses with network information)

## 기본 개념

`ipaddress` 모듈은 세 가지 주요 클래스를 제공합니다:

1. `IPv4Address`와 `IPv6Address`: 개별 IP 주소를 나타냅니다
2. `IPv4Network`와 `IPv6Network`: IP 네트워크(서브넷 마스크 포함)를 나타냅니다
3. `IPv4Interface`와 `IPv6Interface`: IP 인터페이스(네트워크 정보가 있는 주소)를 나타냅니다

## Working with IP Addresses

### Creating IP Address Objects

```python
import ipaddress

# Create IPv4 address
ipv4_addr = ipaddress.IPv4Address('192.168.1.1')
print(ipv4_addr)  # 192.168.1.1

# Create IPv6 address
ipv6_addr = ipaddress.IPv6Address('2001:db8::1')
print(ipv6_addr)  # 2001:db8::1

# Using integer representation
ipv4_from_int = ipaddress.IPv4Address(3232235777)  # 192.168.1.1 as integer
print(ipv4_from_int)  # 192.168.1.1

# Using bytes representation
ipv4_from_bytes = ipaddress.IPv4Address(b'\xC0\xA8\x01\x01')  # 192.168.1.1 as bytes
print(ipv4_from_bytes)  # 192.168.1.1
```

### IP 주소 다루기

### IP 주소 객체 생성하기

```python
import ipaddress

# IPv4 주소 생성
ipv4_addr = ipaddress.IPv4Address('192.168.1.1')
print(ipv4_addr)  # 192.168.1.1

# IPv6 주소 생성
ipv6_addr = ipaddress.IPv6Address('2001:db8::1')
print(ipv6_addr)  # 2001:db8::1

# 정수 표현 사용
ipv4_from_int = ipaddress.IPv4Address(3232235777)  # 정수로 표현된 192.168.1.1
print(ipv4_from_int)  # 192.168.1.1

# 바이트 표현 사용
ipv4_from_bytes = ipaddress.IPv4Address(b'\xC0\xA8\x01\x01')  # 바이트로 표현된 192.168.1.1
print(ipv4_from_bytes)  # 192.168.1.1
```

### Address Validation

The module automatically validates addresses when creating objects:

```python
try:
    invalid_addr = ipaddress.IPv4Address('192.168.300.1')
except ValueError as e:
    print(f"Error: {e}")  # Error: 192.168.300.1 does not appear to be an IPv4 address

# Using factory function for automatic IP version detection
valid_ip = ipaddress.ip_address('192.168.1.1')  # Returns IPv4Address object
valid_ip6 = ipaddress.ip_address('::1')  # Returns IPv6Address object
```

### 주소 유효성 검사

이 모듈은 객체를 생성할 때 자동으로 주소의 유효성을 검사합니다:

```python
try:
    invalid_addr = ipaddress.IPv4Address('192.168.300.1')
except ValueError as e:
    print(f"오류: {e}")  # 오류: 192.168.300.1 does not appear to be an IPv4 address

# 자동 IP 버전 감지를 위한 팩토리 함수 사용
valid_ip = ipaddress.ip_address('192.168.1.1')  # IPv4Address 객체 반환
valid_ip6 = ipaddress.ip_address('::1')  # IPv6Address 객체 반환
```

### Address Properties

```python
ipv4 = ipaddress.IPv4Address('192.168.1.1')
print(f"Version: {ipv4.version}")  # Version: 4
print(f"Max prefixlen: {ipv4.max_prefixlen}")  # Max prefixlen: 32
print(f"Is private: {ipv4.is_private}")  # Is private: True
print(f"Is global: {ipv4.is_global}")  # Is global: False
print(f"Is multicast: {ipv4.is_multicast}")  # Is multicast: False
print(f"Is loopback: {ipv4.is_loopback}")  # Is loopback: False
print(f"Packed form: {ipv4.packed}")  # Packed form: b'\xc0\xa8\x01\x01'
print(f"Integer value: {int(ipv4)}")  # Integer value: 3232235777

ipv6 = ipaddress.IPv6Address('2001:db8::1')
print(f"Is link-local: {ipv6.is_link_local}")  # Is link-local: False
print(f"Exploded form: {ipv6.exploded}")  # Exploded form: 2001:0db8:0000:0000:0000:0000:0000:0001
print(f"Compressed form: {ipv6.compressed}")  # Compressed form: 2001:db8::1
```

### 주소 속성

```python
ipv4 = ipaddress.IPv4Address('192.168.1.1')
print(f"버전: {ipv4.version}")  # 버전: 4
print(f"최대 프리픽스 길이: {ipv4.max_prefixlen}")  # 최대 프리픽스 길이: 32
print(f"사설 IP 여부: {ipv4.is_private}")  # 사설 IP 여부: True
print(f"공인 IP 여부: {ipv4.is_global}")  # 공인 IP 여부: False
print(f"멀티캐스트 여부: {ipv4.is_multicast}")  # 멀티캐스트 여부: False
print(f"루프백 여부: {ipv4.is_loopback}")  # 루프백 여부: False
print(f"패킹된 형태: {ipv4.packed}")  # 패킹된 형태: b'\xc0\xa8\x01\x01'
print(f"정수 값: {int(ipv4)}")  # 정수 값: 3232235777

ipv6 = ipaddress.IPv6Address('2001:db8::1')
print(f"링크-로컬 여부: {ipv6.is_link_local}")  # 링크-로컬 여부: False
print(f"확장된 형태: {ipv6.exploded}")  # 확장된 형태: 2001:0db8:0000:0000:0000:0000:0000:0001
print(f"압축된 형태: {ipv6.compressed}")  # 압축된 형태: 2001:db8::1
```

### Address Operations

```python
# Addition and subtraction
addr1 = ipaddress.IPv4Address('192.168.1.1')
addr2 = addr1 + 5  # 192.168.1.6
addr3 = addr1 - 1  # 192.168.1.0

# Comparison
print(addr1 < addr2)  # True
print(addr1 == ipaddress.IPv4Address('192.168.1.1'))  # True

# Iterations
for ip in range(int(addr1), int(addr1) + 5):
    print(ipaddress.IPv4Address(ip))
# Output:
# 192.168.1.1
# 192.168.1.2
# 192.168.1.3
# 192.168.1.4
# 192.168.1.5
```

### 주소 연산

```python
# 덧셈과 뺄셈
addr1 = ipaddress.IPv4Address('192.168.1.1')
addr2 = addr1 + 5  # 192.168.1.6
addr3 = addr1 - 1  # 192.168.1.0

# 비교
print(addr1 < addr2)  # True
print(addr1 == ipaddress.IPv4Address('192.168.1.1'))  # True

# 반복
for ip in range(int(addr1), int(addr1) + 5):
    print(ipaddress.IPv4Address(ip))
# 출력:
# 192.168.1.1
# 192.168.1.2
# 192.168.1.3
# 192.168.1.4
# 192.168.1.5
```

## Working with Networks

### Creating Network Objects

```python
# Create a network with CIDR notation
network = ipaddress.IPv4Network('192.168.1.0/24')
print(network)  # 192.168.1.0/24

# Alternative notation with netmask
network = ipaddress.IPv4Network('192.168.1.0/255.255.255.0')
print(network)  # 192.168.1.0/24

# Create a network from an address (strict=False allows non-network addresses)
network = ipaddress.IPv4Network('192.168.1.25/24', strict=False)
print(network)  # 192.168.1.0/24

# Factory function for automatic detection
net4 = ipaddress.ip_network('192.168.1.0/24')  # IPv4Network
net6 = ipaddress.ip_network('2001:db8::/64')   # IPv6Network
```

## 네트워크 다루기

### 네트워크 객체 생성하기

```python
# CIDR 표기법으로 네트워크 생성
network = ipaddress.IPv4Network('192.168.1.0/24')
print(network)  # 192.168.1.0/24

# 넷마스크를 사용한 대체 표기법
network = ipaddress.IPv4Network('192.168.1.0/255.255.255.0')
print(network)  # 192.168.1.0/24

# 주소에서 네트워크 생성(strict=False는 비 네트워크 주소 허용)
network = ipaddress.IPv4Network('192.168.1.25/24', strict=False)
print(network)  # 192.168.1.0/24

# 자동 감지를 위한 팩토리 함수
net4 = ipaddress.ip_network('192.168.1.0/24')  # IPv4Network
net6 = ipaddress.ip_network('2001:db8::/64')   # IPv6Network
```

### Network Properties

```python
network = ipaddress.IPv4Network('192.168.1.0/24')

print(f"Network address: {network.network_address}")  # Network address: 192.168.1.0
print(f"Broadcast address: {network.broadcast_address}")  # Broadcast address: 192.168.1.255
print(f"Netmask: {network.netmask}")  # Netmask: 255.255.255.0
print(f"Hostmask: {network.hostmask}")  # Hostmask: 0.0.0.255
print(f"Prefix length: {network.prefixlen}")  # Prefix length: 24
print(f"Number of addresses: {network.num_addresses}")  # Number of addresses: 256
print(f"Is private: {network.is_private}")  # Is private: True

# For IPv6:
net6 = ipaddress.IPv6Network('2001:db8::/64')
print(f"IPv6 network: {net6}")  # IPv6 network: 2001:db8::/64
print(f"IPv6 number of addresses: {net6.num_addresses}")  # IPv6 number of addresses: 18446744073709551616
```

### 네트워크 속성

```python
network = ipaddress.IPv4Network('192.168.1.0/24')

print(f"네트워크 주소: {network.network_address}")  # 네트워크 주소: 192.168.1.0
print(f"브로드캐스트 주소: {network.broadcast_address}")  # 브로드캐스트 주소: 192.168.1.255
print(f"넷마스크: {network.netmask}")  # 넷마스크: 255.255.255.0
print(f"호스트마스크: {network.hostmask}")  # 호스트마스크: 0.0.0.255
print(f"프리픽스 길이: {network.prefixlen}")  # 프리픽스 길이: 24
print(f"주소 개수: {network.num_addresses}")  # 주소 개수: 256
print(f"사설 네트워크 여부: {network.is_private}")  # 사설 네트워크 여부: True

# IPv6의 경우:
net6 = ipaddress.IPv6Network('2001:db8::/64')
print(f"IPv6 네트워크: {net6}")  # IPv6 네트워크: 2001:db8::/64
print(f"IPv6 주소 개수: {net6.num_addresses}")  # IPv6 주소 개수: 18446744073709551616
```

### Iterating Over Networks

```python
# Iterate over all addresses in a network (use with caution for large networks)
network = ipaddress.IPv4Network('192.168.1.0/29')
for address in network:
    print(address)
# Output:
# 192.168.1.0
# 192.168.1.1
# 192.168.1.2
# 192.168.1.3
# 192.168.1.4
# 192.168.1.5
# 192.168.1.6
# 192.168.1.7

# Iterate over hosts only (excluding network and broadcast addresses)
for host in network.hosts():
    print(host)
# Output:
# 192.168.1.1
# 192.168.1.2
# 192.168.1.3
# 192.168.1.4
# 192.168.1.5
# 192.168.1.6

# Get a specific address by index
address = network[5]  # 192.168.1.5
```

### 네트워크 반복하기

```python
# 네트워크의 모든 주소 반복하기(대형 네트워크의 경우 주의해서 사용)
network = ipaddress.IPv4Network('192.168.1.0/29')
for address in network:
    print(address)
# 출력:
# 192.168.1.0
# 192.168.1.1
# 192.168.1.2
# 192.168.1.3
# 192.168.1.4
# 192.168.1.5
# 192.168.1.6
# 192.168.1.7

# 호스트만 반복(네트워크 및 브로드캐스트 주소 제외)
for host in network.hosts():
    print(host)
# 출력:
# 192.168.1.1
# 192.168.1.2
# 192.168.1.3
# 192.168.1.4
# 192.168.1.5
# 192.168.1.6

# 인덱스로 특정 주소 가져오기
address = network[5]  # 192.168.1.5
```

### Network Membership

```python
network = ipaddress.IPv4Network('192.168.1.0/24')
address = ipaddress.IPv4Address('192.168.1.42')

print(address in network)  # True

address2 = ipaddress.IPv4Address('192.168.2.1')
print(address2 in network)  # False

# Using the factory functions
print(ipaddress.ip_address('192.168.1.42') in ipaddress.ip_network('192.168.1.0/24'))  # True
```

### 네트워크 멤버십

```python
network = ipaddress.IPv4Network('192.168.1.0/24')
address = ipaddress.IPv4Address('192.168.1.42')

print(address in network)  # True

address2 = ipaddress.IPv4Address('192.168.2.1')
print(address2 in network)  # False

# 팩토리 함수 사용하기
print(ipaddress.ip_address('192.168.1.42') in ipaddress.ip_network('192.168.1.0/24'))  # True
```

## Network Interfaces

The `IPv4Interface` and `IPv6Interface` classes represent an IP address on a network:

```python
# Create an interface
interface = ipaddress.IPv4Interface('192.168.1.5/24')

# Access address and network components
print(f"IP address: {interface.ip}")  # IP address: 192.168.1.5
print(f"Network: {interface.network}")  # Network: 192.168.1.0/24
print(f"Netmask: {interface.netmask}")  # Netmask: 255.255.255.0
print(f"With hostmask: {interface.with_hostmask}")  # With hostmask: 192.168.1.5/0.0.0.255
print(f"With netmask: {interface.with_netmask}")  # With netmask: 192.168.1.5/255.255.255.0

# Factory function
interface = ipaddress.ip_interface('10.0.0.1/24')  # IPv4Interface
```

## 네트워크 인터페이스

`IPv4Interface`와 `IPv6Interface` 클래스는 네트워크의 IP 주소를 나타냅니다:

```python
# 인터페이스 생성
interface = ipaddress.IPv4Interface('192.168.1.5/24')

# 주소 및 네트워크 구성 요소 접근
print(f"IP 주소: {interface.ip}")  # IP 주소: 192.168.1.5
print(f"네트워크: {interface.network}")  # 네트워크: 192.168.1.0/24
print(f"넷마스크: {interface.netmask}")  # 넷마스크: 255.255.255.0
print(f"호스트마스크 표기: {interface.with_hostmask}")  # 호스트마스크 표기: 192.168.1.5/0.0.0.255
print(f"넷마스크 표기: {interface.with_netmask}")  # 넷마스크 표기: 192.168.1.5/255.255.255.0

# 팩토리 함수
interface = ipaddress.ip_interface('10.0.0.1/24')  # IPv4Interface
```

## Subnetting and Supernetting

### Subnetting

```python
# Subdivide a network into smaller subnets
network = ipaddress.IPv4Network('192.168.1.0/24')
subnets = list(network.subnets())
print(f"Number of /25 subnets: {len(subnets)}")  # Number of /25 subnets: 2
print(f"First subnet: {subnets[0]}")  # First subnet: 192.168.1.0/25
print(f"Second subnet: {subnets[1]}")  # Second subnet: 192.168.1.128/25

# Specify the prefix length
subnets = list(network.subnets(prefixlen_diff=2))  # Create /26 networks
print(f"Number of /26 subnets: {len(subnets)}")  # Number of /26 subnets: 4
for subnet in subnets:
    print(subnet)
# Output:
# 192.168.1.0/26
# 192.168.1.64/26
# 192.168.1.128/26
# 192.168.1.192/26

# Or specify the new prefix directly
subnets = list(network.subnets(new_prefix=28))  # Create /28 networks
print(f"Number of /28 subnets: {len(subnets)}")  # Number of /28 subnets: 16
```

## 서브넷팅과 슈퍼넷팅

### 서브넷팅

```python
# 네트워크를 더 작은 서브넷으로 분할
network = ipaddress.IPv4Network('192.168.1.0/24')
subnets = list(network.subnets())
print(f"/25 서브넷 개수: {len(subnets)}")  # /25 서브넷 개수: 2
print(f"첫 번째 서브넷: {subnets[0]}")  # 첫 번째 서브넷: 192.168.1.0/25
print(f"두 번째 서브넷: {subnets[1]}")  # 두 번째 서브넷: 192.168.1.128/25

# 프리픽스 길이 지정
subnets = list(network.subnets(prefixlen_diff=2))  # /26 네트워크 생성
print(f"/26 서브넷 개수: {len(subnets)}")  # /26 서브넷 개수: 4
for subnet in subnets:
    print(subnet)
# 출력:
# 192.168.1.0/26
# 192.168.1.64/26
# 192.168.1.128/26
# 192.168.1.192/26

# 또는 새 프리픽스를 직접 지정
subnets = list(network.subnets(new_prefix=28))  # /28 네트워크 생성
print(f"/28 서브넷 개수: {len(subnets)}")  # /28 서브넷 개수: 16
```

### Supernetting

```python
# Combine networks into a larger one
net1 = ipaddress.IPv4Network('192.168.1.0/25')
net2 = ipaddress.IPv4Network('192.168.1.128/25')

# Find the supernet that contains both networks
supernet = net1.supernet()  # 192.168.1.0/24

# Verify both networks are contained in the supernet
print(net1.subnet_of(supernet))  # True
print(net2.subnet_of(supernet))  # True

# Or specify the new prefix
supernet = net1.supernet(prefixlen_diff=2)  # 192.168.0.0/23
print(supernet)

# Collapse a list of networks into the smallest possible list of supernets
networks = [
    ipaddress.IPv4Network('192.168.1.0/28'),
    ipaddress.IPv4Network('192.168.1.16/28'),
    ipaddress.IPv4Network('192.168.1.32/28'),
    ipaddress.IPv4Network('192.168.1.48/28'),
]
collapsed = ipaddress.collapse_addresses(networks)
for net in collapsed:
    print(net)  # 192.168.1.0/26
```

### 슈퍼넷팅

```python
# 네트워크를 더 큰 하나로 결합
net1 = ipaddress.IPv4Network('192.168.1.0/25')
net2 = ipaddress.IPv4Network('192.168.1.128/25')

# 두 네트워크를 모두 포함하는 슈퍼넷 찾기
supernet = net1.supernet()  # 192.168.1.0/24

# 두 네트워크가 슈퍼넷에 포함되는지 확인
print(net1.subnet_of(supernet))  # True
print(net2.subnet_of(supernet))  # True

# 또는 새 프리픽스 지정
supernet = net1.supernet(prefixlen_diff=2)  # 192.168.0.0/23
print(supernet)

# 네트워크 목록을 가능한 가장 작은 슈퍼넷 목록으로 축소
networks = [
    ipaddress.IPv4Network('192.168.1.0/28'),
    ipaddress.IPv4Network('192.168.1.16/28'),
    ipaddress.IPv4Network('192.168.1.32/28'),
    ipaddress.IPv4Network('192.168.1.48/28'),
]
collapsed = ipaddress.collapse_addresses(networks)
for net in collapsed:
    print(net)  # 192.168.1.0/26
```

## Practical Examples

### Network Scanning

```python
def scan_network(network_str):
    """Simulate scanning a network by printing all available hosts."""
    try:
        network = ipaddress.ip_network(network_str)
        print(f"Scanning network: {network}")
        print(f"Network address: {network.network_address}")
        print(f"Broadcast address: {network.broadcast_address}")
        print(f"Total addresses: {network.num_addresses}")
        
        # Only print host addresses for small networks
        if network.num_addresses < 1000:
            print("\nAvailable host addresses:")
            for i, host in enumerate(network.hosts()):
                print(f"Host {i+1}: {host}")
        else:
            print(f"\nToo many addresses to display ({network.num_addresses}).")
            
    except ValueError as e:
        print(f"Invalid network address: {e}")

# Example usage
scan_network('192.168.1.0/29')
```

## 실용적인 예제

### 네트워크 스캐닝

```python
def scan_network(network_str):
    """네트워크를 스캔하여 모든 사용 가능한 호스트를 출력하는 시뮬레이션."""
    try:
        network = ipaddress.ip_network(network_str)
        print(f"네트워크 스캔 중: {network}")
        print(f"네트워크 주소: {network.network_address}")
        print(f"브로드캐스트 주소: {network.broadcast_address}")
        print(f"총 주소 수: {network.num_addresses}")
        
        # 작은 네트워크에 대해서만 호스트 주소 출력
        if network.num_addresses < 1000:
            print("\n사용 가능한 호스트 주소:")
            for i, host in enumerate(network.hosts()):
                print(f"호스트 {i+1}: {host}")
        else:
            print(f"\n표시할 주소가 너무 많습니다({network.num_addresses}).")
            
    except ValueError as e:
        print(f"잘못된 네트워크 주소: {e}")

# 사용 예
scan_network('192.168.1.0/29')
```

### IP Address Validation

```python
def validate_ip(ip_str):
    """Validate an IP address and return information about it."""
    try:
        ip = ipaddress.ip_address(ip_str)
        
        result = {
            "valid": True,
            "version": ip.version,
            "is_private": ip.is_private,
            "is_global": ip.is_global,
            "is_multicast": ip.is_multicast,
            "is_loopback": ip.is_loopback,
            "reverse_pointer": ip.reverse_pointer if hasattr(ip, "reverse_pointer") else None
        }
        
        # Add IPv6-specific properties if applicable
        if ip.version == 6:
            result.update({
                "is_link_local": ip.is_link_local,
                "is_site_local": ip.is_site_local,
                "ipv4_mapped": ip.ipv4_mapped is not None
            })
            
        return result
    except ValueError:
        return {"valid": False}

# Example usage
ips_to_check = ['192.168.1.1', '10.0.0.1', '256.0.0.1', '2001:db8::1', '::1']
for ip in ips_to_check:
    result = validate_ip(ip)
    if result["valid"]:
        print(f"{ip}: Valid IPv{result['version']} address")
        print(f"  Private: {result['is_private']}")
        print(f"  Global: {result['is_global']}")
    else:
        print(f"{ip}: Invalid IP address")
```

### IP 주소 유효성 검사

```python
def validate_ip(ip_str):
    """IP 주소를 검증하고 그에 대한 정보를 반환합니다."""
    try:
        ip = ipaddress.ip_address(ip_str)
        
        result = {
            "valid": True,
            "version": ip.version,
            "is_private": ip.is_private,
            "is_global": ip.is_global,
            "is_multicast": ip.is_multicast,
            "is_loopback": ip.is_loopback,
            "reverse_pointer": ip.reverse_pointer if hasattr(ip, "reverse_pointer") else None
        }
        
        # 해당되는 경우 IPv6 특정 속성 추가
        if ip.version == 6:
            result.update({
                "is_link_local": ip.is_link_local,
                "is_site_local": ip.is_site_local,
                "ipv4_mapped": ip.ipv4_mapped is not None
            })
            
        return result
    except ValueError:
        return {"valid": False}

# 사용 예
ips_to_check = ['192.168.1.1', '10.0.0.1', '256.0.0.1', '2001:db8::1', '::1']
for ip in ips_to_check:
    result = validate_ip(ip)
    if result["valid"]:
        print(f"{ip}: 유효한 IPv{result['version']} 주소")
        print(f"  사설 IP: {result['is_private']}")
        print(f"  공인 IP: {result['is_global']}")
    else:
        print(f"{ip}: 잘못된 IP 주소")
```

### CIDR Calculator

```python
def cidr_calculator(cidr_str):
    """Calculate and display network information from CIDR notation."""
    try:
        network = ipaddress.ip_network(cidr_str)
        
        print(f"Network: {network}")
        print(f"Network address: {network.network_address}")
        print(f"Broadcast address: {network.broadcast_address}")
        print(f"Netmask: {network.netmask}")
        print(f"Hostmask: {network.hostmask}")
        print(f"Prefix length: {network.prefixlen}")
        print(f"Number of addresses: {network.num_addresses}")
        print(f"Usable hosts: {network.num_addresses - 2 if network.version == 4 else network.num_addresses}")
        
        # First and last usable host (for IPv4)
        if network.version == 4 and network.num_addresses > 2:
            hosts = list(network.hosts())
            print(f"First usable host: {hosts[0]}")
            print(f"Last usable host: {hosts[-1]}")
            
        # Subnet information
        if network.prefixlen < network.max_prefixlen - 1:
            print("\nSubnetting Information:")
            print(f"Next subnet level (+1): {list(network.subnets())[0]} and {list(network.subnets())[1]}")
        
        # Supernet information
        if network.prefixlen > 0:
            supernet = network.supernet()
            print(f"\nSupernet: {supernet}")
            print(f"This network is 1 of {2**(supernet.prefixlen - network.prefixlen)} subnets in {supernet}")
            
    except ValueError as e:
        print(f"Invalid CIDR notation: {e}")

# Example usage
cidr_calculator('192.168.1.0/28')
```

### CIDR 계산기

```python
def cidr_calculator(cidr_str):
    """CIDR 표기법에서 네트워크 정보를 계산하고 표시합니다."""
    try:
        network = ipaddress.ip_network(cidr_str)
        
        print(f"네트워크: {network}")
        print(f"네트워크 주소: {network.network_address}")
        print(f"브로드캐스트 주소: {network.broadcast_address}")
        print(f"넷마스크: {network.netmask}")
        print(f"호스트마스크: {network.hostmask}")
        print(f"프리픽스 길이: {network.prefixlen}")
        print(f"주소 개수: {network.num_addresses}")
        print(f"사용 가능한 호스트: {network.num_addresses - 2 if network.version == 4 else network.num_addresses}")
        
        # 첫 번째 및 마지막 사용 가능한 호스트(IPv4의 경우)
        if network.version == 4 and network.num_addresses > 2:
            hosts = list(network.hosts())
            print(f"첫 번째 사용 가능한 호스트: {hosts[0]}")
            print(f"마지막 사용 가능한 호스트: {hosts[-1]}")
            
        # 서브넷 정보
        if network.prefixlen < network.max_prefixlen - 1:
            print("\n서브넷 정보:")
            print(f"다음 서브넷 레벨(+1): {list(network.subnets())[0]} 및 {list(network.subnets())[1]}")
        
        # 슈퍼넷 정보
        if network.prefixlen > 0:
            supernet = network.supernet()
            print(f"\n슈퍼넷: {supernet}")
            print(f"이 네트워크는 {supernet} 내에 있는 {2**(supernet.prefixlen - network.prefixlen)}개 서브넷 중 하나입니다")
            
    except ValueError as e:
        print(f"잘못된 CIDR 표기법: {e}")

# 사용 예
cidr_calculator('192.168.1.0/28')
```

## Best Practices

1. **Use the factory functions**: The `ip_address()`, `ip_network()`, and `ip_interface()` functions automatically determine whether you're working with IPv4 or IPv6.

2. **Handle exceptions**: Always wrap IP creation in try-except blocks to handle invalid inputs gracefully.

3. **Be careful with large networks**: Iterating over large networks can consume significant memory and CPU. Consider alternative approaches for large networks.

4. **Use strict=False when appropriate**: When creating networks from addresses, use `strict=False` to automatically convert addresses to network addresses.

5. **Leverage built-in attributes**: The `ipaddress` module provides many useful attributes for categorizing addresses (private, loopback, etc.), which can simplify your code.

## 모범 사례

1. **팩토리 함수 사용하기**: `ip_address()`, `ip_network()`, `ip_interface()` 함수는 IPv4 또는 IPv6를 자동으로 판별합니다.

2. **예외 처리하기**: 항상 IP 생성을 try-except 블록으로 감싸서 잘못된 입력을 우아하게 처리하세요.

3. **대규모 네트워크 주의하기**: 대규모 네트워크를 반복하면 상당한 메모리와 CPU를 소모할 수 있습니다. 대규모 네트워크의 경우 대체 접근 방식을 고려하세요.

4. **적절한 경우 strict=False 사용하기**: 주소에서 네트워크를 생성할 때 `strict=False`를 사용하여 주소를 네트워크 주소로 자동 변환하세요.

5. **내장 속성 활용하기**: `ipaddress` 모듈은 주소를 분류하기 위한 많은 유용한 속성(사설, 루프백 등)을 제공하여 코드를 단순화할 수 있습니다.

## Conclusion

The `ipaddress` module is a powerful tool for working with IP addresses and networks in Python. It provides a comprehensive set of features for:

- Creating and validating IP addresses and networks
- Examining properties of addresses and networks
- Performing complex operations like subnetting and supernetting
- Testing relationships between addresses and networks

Whether you're writing network management tools, implementing security checks, or simply need to validate user input, the `ipaddress` module offers a clean, Pythonic interface for all your IP addressing needs.

## 결론

`ipaddress` 모듈은 Python에서 IP 주소와 네트워크를 다루기 위한 강력한 도구입니다. 다음과 같은 포괄적인 기능을 제공합니다:

- IP 주소 및 네트워크 생성 및 유효성 검사
- 주소 및 네트워크의 속성 검사
- 서브넷팅 및 슈퍼넷팅과 같은 복잡한 작업 수행
- 주소와 네트워크 간의 관계 테스트

네트워크 관리 도구를 작성하든, 보안 검사를 구현하든, 단순히 사용자 입력의 유효성을 검사해야 하든, `ipaddress` 모듈은 모든 IP 주소 지정 요구 사항에 대해 깔끔하고 Pythonic한 인터페이스를 제공합니다.
