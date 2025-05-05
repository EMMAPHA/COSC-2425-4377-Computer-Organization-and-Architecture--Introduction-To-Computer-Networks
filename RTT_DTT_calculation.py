
estimated_rtt = 360.0  
dev_rtt = 40.0         
sample_rtt = 430.0     
alpha = 0.115
beta = 0.025
# Compute new EstimatedRTT
estimated_rtt_new = (1 - alpha) * estimated_rtt + alpha * sample_rtt
# Compute new DevRTT
dev_rtt_new = (1 - beta) * dev_rtt + beta * abs(sample_rtt - estimated_rtt)
# Compute TimeoutInterval
timeout_interval = estimated_rtt_new + 4 * dev_rtt_new
print(f"New EstimatedRTT: {estimated_rtt_new:.2f} ms")
print(f"New DevRTT: {dev_rtt_new:.2f} ms")
print(f"New TimeoutInterval: {timeout_interval:.2f} ms")