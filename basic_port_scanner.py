import socket

def scan_port(target, port):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(1)
		
		result = s.connect_ex((target, port))
		
		if result == 0:
			print(f"[OPEN] Port {port}")
		else:
			print(f"[CLOSED] Port {port}")
			
			s.close()
			
	except Exception as e:
		print(f"[ERROR] Port {port} : {e}")
			
def main():
	target = input("Enter Targets IP : ")
	
	print(f" \n Scanning {target}.... \n")
	
	for port in range (1, 8001):
		scan_port (target, port)
		
if __name__ == "__main__":
	main()
