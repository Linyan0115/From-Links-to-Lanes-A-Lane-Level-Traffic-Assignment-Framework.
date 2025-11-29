import osmnx as ox
import pandas as pd


G = ox.graph_from_place("Sioux Falls, South Dakota, USA", network_type="drive")


G = ox.add_edge_speeds(G)
G = ox.add_edge_travel_times(G)


links = []
link_id = 1
for u, v, k, data in G.edges(keys=True, data=True):
    # 节点 o, d
    o = u
    d = v


    ta = data.get("travel_time", None)  # 秒

    # 车道数（缺省时设为1）
    lanes = data.get("lanes")
    try:
        lanes = int(lanes)
    except:
        lanes = 1

    # 假设每车道容量 2000 veh/hour
    per_lane_capacity = 2000

    # 道路等级
    road_type = data.get("highway", "unknown")

    # 为每条 lane 生成一个 link
    for lane_idx in range(1, lanes + 1):
        links.append({
            "id": link_id,
            "o": o,
            "d": d,
            "ta": ta,
            "ca": per_lane_capacity,   # 每车道单独容量
            "lane_level": lane_idx,
            "road_type": road_type
        })
        link_id += 1

# 3. 转换为 DataFrame
df_links = pd.DataFrame(links)

# 4. 保存
df_links.to_csv("sioux_falls_lane_links_with_roadtype.csv", index=False)
print(df_links.head(10))


