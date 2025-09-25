from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier,export_text
from sklearn.model_selection import train_test_split

wine= load_wine()
X,y=wine.data, wine.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


tree = DecisionTreeClassifier(max_depth=None, random_state=42)
tree.fit(X_train, y_train)


rules = export_text(tree, feature_names=wine.feature_names)
print(" Reglas del árbol de decisión (max_depth=2):\n")
print(rules)


print("\n Precisión en datos de prueba:", tree.score(X_test, y_test))
