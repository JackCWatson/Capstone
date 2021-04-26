#Jack Watson
import speedtest

servers = []

#pip install speedtest-cli
# API courtesey of github user sivel

s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()
s.download()
s.upload()

results_dict = s.results.dict()

##print(s.results.share())



d = int(results_dict['download']) / 1000000
u = int(results_dict['upload']) / 1000000
p = float(results_dict['ping'])

print("Download: " + ('%.2f'%d) + " mb/s") 
print("Upload: " + ('%.2f'%u) + " mb/s") 
print("Ping: " + str(round(p)) + " ms")

print("Done")