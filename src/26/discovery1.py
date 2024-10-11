import py_eureka_client.eureka_client as eureka_client

eureka_client.init(eureka_server="http://localhost:8761/eureka",
                   app_name="discovery1",
                   instance_port=8000)

client = eureka_client.get_client()
for app in client.applications.applications:
    print(vars(app))
    for ins in app.instances:
        print("[%s] %s:%d" % (ins.instanceId, ins.ipAddr, ins.port.port))
                
# res = eureka_client.do_service("test1", "/get_events?start=2024-10-06T00:00:00&end=2024-10-13T00:00:00")
res = eureka_client.do_service(app_name="BOB", service="/") #, prefer_ip=True) #, return_type="string")
print("result:" + res)                   
