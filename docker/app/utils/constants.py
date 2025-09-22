from datetime import datetime

DATE_FORK = datetime(2011, 5, 19)

FOLDER_TO_SAVE_RESULT = "/app/storage"

PAST_IN_SIZE = 17
FUTURE_IN_SIZE = 20

P_OUT_SIZE = 30
HE_OUT_SIZE = 26

P_PAST_MLP_MODEL_PATH = "/app/models/jit_p_linear_model_past.pt"
P_FUTURE_MLP_MODEL_PATH = "/app/models/jit_p_linear_model.pt"
P_PAST_CNN_MODEL_PATH = "/app/models/jit_p_cnn_model_past.pt"
P_FUTURE_CNN_MODEL_PATH = "/app/models/jit_p_cnn_model.pt"
HE_PAST_MLP_MODEL_PATH = "/app/models/jit_he_linear_model_past.pt"
HE_FUTURE_MLP_MODEL_PATH = "/app/models/jit_he_linear_model.pt"
HE_PAST_CNN_MODEL_PATH = "/app/models/jit_he_cnn_model_past.pt"
HE_FUTURE_CNN_MODEL_PATH = "/app/models/jit_he_cnn_model.pt"

P_PAST_PROCESSORS_PATH = "/app/models/scalers/p_scalers_past(0-features, 1-target).pkl"
P_FUTURE_PROCESSORS_PATH = "/app/models/scalers/p_scalers(0-features, 1-target).pkl"
HE_PAST_PROCESSORS_PATH = (
    "/app/models/scalers/he_scalers_past(0-features, 1-target).pkl"
)
HE_FUTURE_PROCESSORS_PATH = "/app/models/scalers/he_scalers(0-features, 1-target).pkl"
