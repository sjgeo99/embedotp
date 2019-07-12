file = open("part1_EncryptedMsg1.dms", "rb")
encmsg1 = file.readlines()

file2 = open("part2_EncryptedMsg1.dms", "rb")
encmsg2 = file2.readlines()

file3 = open("part1_UnencryptedMsg", "rb")
pltxt1 = file3.readlines()

xord = int(encmsg1, 2) ^ int(encmsg2, 2)

print(xord)
