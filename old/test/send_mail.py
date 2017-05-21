def send_mail(settings, infos):
	settings['sender']
	settings['port']
	settings['smtp']
	settings['sender']
	infos
	infos = [['cpu', 95], ['ram', 100]]
	body = message
	for info in infos:
		body += "\n{} : {}".format(info[0], info[1])
	# envoi

def send_mails(infos):
	configfile = ...
	config = ConfigParser()
	config.read(configfile)
	settings['message'] = config.get('Mail','message')
	for conf in config.sections():
		for key, value in conf.items(conf):
			settings[key] = value
		send_mail(settings, infos)
