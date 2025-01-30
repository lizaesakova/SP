import pandas as pd
import numpy as np
import torch
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import StratifiedKFold, KFold
from sklearn.linear_model import LinearRegression


class Dataset():
    def __init__(self, path_to_file: str):
        self.path = path_to_file
        self.__data = pd.read_csv(self.path)

    def get_data(self):
        return self.__data

    def remove_outliers(self, column: str) -> pd.DataFrame:
        q = self.__data[column].quantile(0.99)
        self.__data = self.__data[self.__data[column] <= q]
        return self.__data

    def filled(self, strategy='mode', value=None):
        for column in self.__data.columns:
            if self.__data[column].isnull().sum() > 0:
                if strategy == 'mode':
                    self.__data[column].fillna(self.__data[column].mode()[0], inplace=True)
                elif strategy == 'mean':
                    self.data[column].fillna(self.data[column].mean(), inplace=True)
                elif strategy == 'median':
                    self.data[column].fillna(self.data[column].median(), inplace=True)
                elif strategy == 'constant' and value is not None:
                    self.__data[column].fillna(value, inplace=True)


    def check_categorical(self, threshold: int = None):

        if threshold is None:
            threshold = self.__data.shape[0]

        categorical_names = []
        for column in self.__data.columns:
            unique_count = self.__data[column].nunique()
            if unique_count <= threshold:
                categorical_names.append(column)
        return categorical_names

    def eval_categorical(self, categorical_names, strategy='OneHot'):

        if strategy == 'Label':
            encoder = LabelEncoder()
            for column in categorical_names:
                self.__data[column] = encoder.fit_transform(self.__data[column])

        elif strategy == 'OneHot':
            encoder = preprocessing.OneHotEncoder()
            for col in categorical_cols:
                one_hot_encoded = encoder.fit_transform(self.__data[[col]])
                one_hot_df = pd.DataFrame(one_hot_encoded, columns=encoder.get_feature_names_out([col]))
                self.__data = pd.concat([self.__data, one_hot_df], axis=1).drop(columns=categorical_names)
        else:
            raise ValueError("choose strategy from the available ones: 'OneHot' or 'Label'.")


    def prep(self, threshold: int = None, strategy='Onehot') -> None:
        self.fill_strategy(strategy='mean')
        categorical_names = self.check_categorical(threshold=threshold)
        self.eval_categorical(categorical_names, strategy)

    def display_stat(self):
        for col in self.__data.select_dtypes(include=['int64', 'float64']).columns:
            print(f"Статистика для колонки '{col}':")
            print(f"Количество ненулевых значений: {self.__data[col].count()}")
            print(f"Среднее значение: {self.__data[col].mean()}")
            print(f"Максимальное значение: {self.__data[col].max()}")
            print(f"Минимальное значение: {self.__data[col].min()}\n")
            self.__data[col].plot(kind='hist', figsize=(10, 5), grid=True, title=f'Гистограмма {col}')
            plt.show()
  
    def transform(self, to_tensor='numpy'):
        if to_tensor == 'numpy':
            return self.X.to_numpy(), self.y.to_numpy()
        elif to_tensor == 'pytorch':
            return torch.tensor(self.X.values, dtype=torch.float32), torch.tensor(self.y.values, dtype=torch.float32)
        elif to_tensor == 'tensorflow':
            return tf.convert_to_tensor(self.X.values, dtype=tf.float32), tf.convert_to_tensor(self.y.values, dtype=tf.float32)
        else:
            raise ValueError("ошибка, формат не поддерживается.")


  
    def cross_validation(self, n_splits=10, stratify_by=None):
       
        def create_stratify_feature(columns):
            stratify_cols = []
            for col in columns:
                if col in self.__categorical_features:
                    stratify_cols.append(self.__data[col].astype(str))
                else:
                    self.__data[f'{col}_binned_feature'] = pd.qcut(self.__data[col], q=5, labels=False)
                    stratify_cols.append(self.__data[f'{col}_binned_feature'].astype(str))
            return '_'.join(stratify_cols)

        if stratify_by:
            if isinstance(stratify_by, list) and all(feature in self.__data.columns for feature in stratify_by):
                stratify_feature = create_stratify_feature(stratify_by)
            elif stratify_by in self.__data.columns:
                stratify_feature = self.__data[stratify_by].astype(str) if stratify_by in self.__categorical_data else pd.qcut(self.__data[stratify_by], q=5, labels=False).astype(str)
            else:
                raise ValueError("Признак для стратификации не найден в данных.")
            
            StrKf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=50)
            splits = StrKf.split(self.__data, stratify_feature)
            return [(self.__data.iloc[train_idx], self.__data.iloc[test_idx]) for train_idx, test_idx in splits]
        
        else:
            kf = KFold(n_splits=n_splits, shuffle=True, random_state=50)
            splits = kf.split(self.__data)
            return [(self.__data.iloc[train_idx], self.__data.iloc[test_idx]) for train_idx, test_idx in splits]  



data1 = Dataset('/content/Mall_Customers.csv')
data1.display_stat()
data1.get_data()

X_np, y_np = data1.transform(to_tensor='numpy')

model = LinearRegression()
data1.cross_validation(n_splits=10, stratify_by=['Age', 'Genre'])
