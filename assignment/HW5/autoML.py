# 라이브러리 Import
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from sklearn.pipeline import Pipeline
import optuna

# ---------------------------
# Step 1: 데이터 로드 및 전처리
# ---------------------------
# 데이터 로드 (Wine Quality Dataset 사용)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
data = pd.read_csv(url, sep=';')

# 데이터 확인
print("Dataset Shape:", data.shape)
print(data.head())

# Feature와 Target 나누기
X = data.drop('quality', axis=1)
y = data['quality']

# 데이터셋 나누기
# 500개 데이터를 Training & Validation 세트로, 나머지는 Test Set으로 분할
X_train_val, X_test, y_train_val, y_test = train_test_split(X, y, train_size=500, random_state=42)

# Training & Validation 세트 내부를 다시 나누기 (Train:Validation = 80:20)
X_train, X_val, y_train, y_val = train_test_split(X_train_val, y_train_val, test_size=0.2, random_state=42)

# ---------------------------
# Step 2: AutoML 파이프라인 구현
# ---------------------------
def objective(trial):
    # 모델 선택
    model_name = trial.suggest_categorical('model', ['RandomForest', 'XGBoost', 'LightGBM'])
    
    # 파이프라인: 스케일러와 모델 연결
    pipeline_steps = [('scaler', StandardScaler())]  # 스케일링
    
    if model_name == 'RandomForest':
        n_estimators = trial.suggest_int('rf_n_estimators', 1, 150, step=10)
        max_depth = trial.suggest_int('rf_max_depth', 3, 10, step=1)
        model = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
        
    elif model_name == 'XGBoost':
        n_estimators = trial.suggest_int('xgb_n_estimators', 1, 150, step=10)
        max_depth = trial.suggest_int('xgb_max_depth', 3, 10, step=1)
        learning_rate = trial.suggest_loguniform('xgb_lr', 0.01, 0.3)
        model = XGBRegressor(n_estimators=n_estimators, max_depth=max_depth, learning_rate=learning_rate, random_state=42)
        
    else:  # LightGBM
        n_estimators = trial.suggest_int('lgb_n_estimators', 1, 150, step=1)
        num_leaves = trial.suggest_int('lgb_num_leaves', 30, 100, step=5)  # 'num_leaves' 값을 높여주기
        learning_rate = trial.suggest_loguniform('lgb_lr', 0.01, 0.2)  # learning_rate 범위 조정
        model = LGBMRegressor(n_estimators=n_estimators, num_leaves=num_leaves, learning_rate=learning_rate, random_state=42)
    
    # 모델을 파이프라인에 추가
    pipeline_steps.append(('model', model))
    pipeline = Pipeline(pipeline_steps)
    
    # 교차 검증을 통한 성능 평가
    score = cross_val_score(pipeline, X_train, y_train, cv=3, scoring='neg_mean_squared_error').mean()
    return -score  # Optuna는 값을 최소화하므로 음수 변환

# Optuna 실행
study = optuna.create_study(direction='minimize')
study.optimize(objective, n_trials=30)

# 최적의 하이퍼파라미터 출력
print("Best Trial:")
print(study.best_trial.params)

# ---------------------------
# Step 3: 최적 모델 학습 및 평가
# ---------------------------
# 최적 모델 학습 및 평가
best_params = study.best_trial.params

# 최적 모델과 Pipeline 재구성
pipeline_steps = [('scaler', StandardScaler())]  # 스케일링
if best_params['model'] == 'RandomForest':
    model = RandomForestRegressor(
        n_estimators=best_params['rf_n_estimators'],
        max_depth=best_params['rf_max_depth'],
        random_state=42
    )
elif best_params['model'] == 'XGBoost':
    model = XGBRegressor(
        n_estimators=best_params['xgb_n_estimators'],
        max_depth=best_params['xgb_max_depth'],
        learning_rate=best_params['xgb_lr'],
        random_state=42
    )
else:  # LightGBM
    model = LGBMRegressor(
        n_estimators=best_params['lgb_n_estimators'],
        num_leaves=best_params['lgb_num_leaves'],
        learning_rate=best_params['lgb_lr'],
        random_state=42
    )

pipeline_steps.append(('model', model))
final_pipeline = Pipeline(pipeline_steps)

# 최적 모델 학습
final_pipeline.fit(X_train, y_train)

# Validation 성능 평가
y_pred_val = final_pipeline.predict(X_val)
val_rmse = mean_squared_error(y_val, y_pred_val, squared=False)
print(f"Validation RMSE: {val_rmse:.4f}")

# Test 세트에서 최종 평가
y_pred_test = final_pipeline.predict(X_test)
test_rmse = mean_squared_error(y_test, y_pred_test, squared=False)
test_r2 = r2_score(y_test, y_pred_test)
print(f"Test RMSE: {test_rmse:.4f}")
print(f"Test R2 Score: {test_r2:.4f}")

# ---------------------------
# Step 4: 결과 요약
# ---------------------------
print("\n===== 최종 결과 =====")
print("최적 모델:", best_params['model'])
print("하이퍼파라미터:", best_params)
print(f"Test RMSE: {test_rmse:.4f}")
print(f"Test R2 Score: {test_r2:.4f}")
