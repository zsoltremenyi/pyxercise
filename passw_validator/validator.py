import getpass
import pwinput
import bcrypt

print(bcrypt)
login = {"dirk": b"$2b$12$qWDVJeKX7DSJRNb7USJLR.KhDB9bj22vkTEMSE4jkLRClHkvB1Z5a", #abc123
         "bubba": b"$2b$12$V1X2mx4fwg411YXMvNtzYevEukJ8SQO.SR5rpucIahLjDtRBLOkIa", #if you find this one out, i'll buy you a beer
         "jacque": b"$2b$12$EjsosXzfTpLO4ihdIgGGau7aR/RCOgziSoiMc/AI/3FiWeFwnKkG", #CsCSSCsC
         }


password = pwinput.pwinput(prompt="What is your password? ", mask="*")


if bcrypt.checkpw(bytes(password, encoding="ascii"), login["dirk"]):
    print("Welcome!")
else:
    print("I don't know you.")

