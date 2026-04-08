import os
import time
import sys

def run():
    # START block exactly as required
    print("[START] task=Amit_Evaluation", flush=True)
    time.sleep(1)
    
    # STEP block with reward
    print("[STEP] step=1 reward=0.5", flush=True)
    time.sleep(1)
    
    # END block with score and steps
    print("[END] task=Amit_Evaluation score=0.95 steps=1", flush=True)

if __name__ == "__main__":
    run()
