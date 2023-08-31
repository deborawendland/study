import synchronization.scheduler as scheduler
import synchronization.synchronization as synchronization
import settings

def main():
    print ("app starting...")
    scheduler.run_scheduler(settings.sync_interval, synchronization.run_sync)

if __name__ == "__main__":
    main()