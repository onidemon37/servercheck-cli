import asyncio
import requests
import os


def get(server):
    debug = os.getenv("DEBUG")
    try:
        if debug:
            print(f"Making request to {server}")
        response = requests.get(f"http://{server}")
        if debug:
            print(f"Received response from server {server}")
        return {"status_code": response.status_code, "server": server}
    except:
        if debug:
            print(f"Failed to connect to {server}")
        return {"status_code": -1, "server": server}


async def ping(server, results):
    loop = asyncio.get_event_loop()
    future_result = loop.run_in_executor(None, get, server)
    result = await future_result
    if result["status_code"] in range(200, 299):
        results["success"].append(server)
    else:
        results["failure"].append(server)


async def make_requests(servers, results):
    tasks = []

    for server in servers:
        task = asyncio.create_task(ping(server, results))
        tasks.append(task)

    await asyncio.gather(*tasks)


def ping_servers(servers):
    results = {"success": [], "failure": []}
    asyncio.run(make_requests(servers, results))
    return results
