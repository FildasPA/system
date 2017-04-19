import psutil

print (" ")

print ("Informations sur les utilisateurs : ")
users = psutil.users()
print ("Nombre d'utilisateur connecte (peut etre plusieurs fois le meme) : ")
print len(users) #nombre d'utilisateur
length = len(users)
taille = 0
while taille < length:
	if taille < length:
		print(users[taille][0]) #affichage du nom de l'utilisateur
		taille = taille +1
	else:
		print(" ")

print (" ")

print ("Informations sur la RAM (% utilise) : ")
vm = psutil.swap_memory() # RAM -> swap
mem = vm[3]
print (mem)
totmem = vm[0] / 1000000000
print ("Memoire total en GB: ")
print (totmem)
usedmem = vm[1] / 1000000000
print ("Memoire utilisee en GB: ")
print (usedmem)
availmem = vm[2] / 1000000000
print ("Memoire disponible en GB: ")
print (availmem)

print (" ")

print ("Information sur la memoire restante du disque '/' (% utilise) : ")
disk = psutil.disk_usage('/')
disque = disk[3]
print (disque)

print (" ")

print ("Nombre de disques : ")
dis = psutil.disk_partitions()
nbdisk = len(dis)
print (nbdisk)
taille = 0
length = len(dis)
print ("Les disques sont : ")
while taille < length:
	if taille < length:
		print(dis[taille][0]) #affichage du nom de l'utilisateur
		taille = taille +1
	else:
		print(" ")

print (" ")

print ("Nombre de processus lances : ")
pids = psutil.pids()
nbpids = len(pids)
print (nbpids)

print (" ")

