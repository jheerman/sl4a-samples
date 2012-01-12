import android
droid = android.Android()
scan = droid.scanBarcode().result
code = int(scan['extras']['SCAN_RESULT'])
url = "https://www.google.com/search?q=%d&tbm=shop" % code
droid.startActivity('android.intent.action.VIEW', url)
