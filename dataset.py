import pandas as pd
import matplotlib.pyplot as plt
cars=pd.read_csv("C:/dataset1/Cars93.csv")
Columns=["Manufacturer","Model","Type","Price"]
cars[Columns].head(5)
cars["Price"].plot(kind="box",figsize=(10,7))
cars["MPG.city"].plot(kind="hist",figsize=(10,7))
ax=cars.plot(["Horsepower"],["MPG.city"],kind="scatter",marker="o",color="red",figsize=(10,7))
ax.set_xlabel("Horsepower")
ax.set_xlabel("MPG.city")
ax=cars.plot(x="EngineSize",y="Horsepower",kind="line",color="black")
ax.set_xlabel("EngineSize")
ax.set_ylabel("Horsepower")
