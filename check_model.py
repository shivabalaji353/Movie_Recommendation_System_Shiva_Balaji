import pickle

with open("movie_recommender_model.pkl", "rb") as f:
    model = pickle.load(f)

print("=" * 50)
print("Model Type:")
print(type(model))
print("=" * 50)

if isinstance(model, dict):
    print("Keys in the model:")
    for key in model.keys():
        print("-", key)
else:
    print("The model is not a dictionary.")

print("=" * 50)