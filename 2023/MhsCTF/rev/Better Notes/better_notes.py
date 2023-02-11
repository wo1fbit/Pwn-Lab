from base64 import b64encode

valentine = bytes(input("Valentine: "), "utf-8")
a = b64encode(valentine)
b = b64encode(valentine[::-1])
a = list(map(ord, list(str(a))))
b = list(map(ord, list(str(b))))
for j in range(len(a)):
  print(chr((a[j] + b[j]) % 58 + 65), end='')
print("")
