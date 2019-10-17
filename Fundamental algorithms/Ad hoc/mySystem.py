"""
    ...
    /**
     * Waits durationMillis milliseconds then runs the callback.
     *
     * Only one timer can be pending at one time.  If called again before the
     * duration expires, the original timer is overwritten without running
     * callback.
    */
    static void setTimer(long durationMillis, Runnable callback);

    /** Returns the current time in milliseconds since system boot. */
    static long getCurrentTimeMillis();
    
    ...
"""
class MySystem:


"""
/**
 * Waits durationMillis milliseconds then runs the callback.
 *
 * Supports multiple concurrent timers -- calling add_timer will not break
 * any previously started timers.
 */

"""

void addTimer(long durationMillis, Runnable callback);


这个addTimer在MySystem里面。用法如下：
MySystem sys = new MySystem();
sys.addTimer(100, runnable1);
sleep(50)
sys.addTimer(100, runable2);