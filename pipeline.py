import sys
from preprocessor import load_and_prepare

def run_pipeline(filepath):
    print(f"[pipeline] Loading data from: {filepath}")
    df, scaler = load_and_prepare(filepath)

    print(f"[pipeline] Shape after preprocessing: {df.shape}")
    print(f"[pipeline] Columns: {list(df.columns)}")
    print(f"[pipeline] Preview:\n{df.head()}\n")

    # --- DETECTORS ---
    detectors = []
    # EG: ThresholdAD
    # Link to ADTK website for that detector
    # Information regarding implementation
    

    results = {}
    for detector in detectors:
        name = type(detector).__name__
        print(f"[pipeline] Running detector: {name}")
        results[name] = detector.detect(df)

    if not detectors:
        print("[pipeline] Currently no detectors — preprocessing works")

    return df, scaler, results


if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) > 1 else "datasets/complex.csv"
    run_pipeline(filepath)
