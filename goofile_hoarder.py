from goofile.goofile import GooSearch
import os
import requests
from pathlib import Path

def main():
	domain = "www.google.com"
	filetype = "txt"
	key = None
	engine = None
	query = None
	logging = "INFO"

	goo = GooSearch(domain=domain, filetype=filetype, key=key, engine=engine, query=query, log=logging)

	cant = 0
	result = []

	cwd = Path.cwd()
	folderName = 'goofile_hoarder'
	if os.path.isdir(f"{cwd}\\{folderName}") == False:
		os.mkdir(folderName)
	#print(cwd)

	while cant < goo.limit:
	    if getattr(goo, 'key', None) and getattr(goo, 'engine', None):
	        r = goo.run_api(goo)
	    else:
	        r = goo.run_basic()
	    for x in r:
	        if result.count(x) == 0:
	            result.append(x)
	    cant += 100

	for index, link in enumerate(result):
		try:
			if "https://" not in link:
				link = f"https://{link}"
			item = link.replace("/", "-").replace("\\", "-").replace(":", "")
			file = requests.get(link)
			open(f"{cwd}\\{folderName}\\{item}", 'wb').write(file.content)
			#print(f"{index} {link}")
		except Exception as e:
			print(e)
			continue

if __name__ == '__main__':
	main()