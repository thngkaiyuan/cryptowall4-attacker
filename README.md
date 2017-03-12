# CryptoWall4 Attacker

Used in conjunction with [CryptoWall4 C&C](https://github.com/thngkaiyuan/cryptowall4-cnc) to demonstrate DOS attack on a CryptoWall C&C server by leveraging on the resource asymmetrical property of a public key generation request.

## Asymmetrical CPU Utilization (Attacker 3.4% VS C&C 96% with just 1 locust)

Attacker (3.4% CPU Utilization):
![image](https://cloud.githubusercontent.com/assets/10496851/23831185/d8b0e464-0756-11e7-8f2f-be09f1d9fb22.png)

C&C (96% CPU Utilization):
![image](https://cloud.githubusercontent.com/assets/10496851/23831187/00127bc6-0757-11e7-970c-3a8d2677a9d6.png)

## Denial of Service (with 10000 locusts)

10000 locusts causing 80% failure rate:
![image](https://cloud.githubusercontent.com/assets/10496851/23831123/8f428df6-0755-11e7-88f5-3f697d30c60a.png)

On a "victim" machine requesting for a key:
```
$ curl http://172.16.27.130/Zoe2aN.php?b=dp7tm9rl3z09 --data "z=647571383032373074706a3771698a5e1581a9341bf0f0d8cebb252aec8f7338e321aa3c140f55087f3db92351efcf999ce70d063065672d05f86193f9b940"
curl: (56) Recv failure: Operation timed out
```
