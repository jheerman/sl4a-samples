import android
droid = android.Android()
scan = droid.scanBarcode().result
isbn = int(scan['extras']['SCAN_RESULT'])
url = "http://books.google.com?q=%d" % isbn
droid.startActivity('android.intent.action.VIEW', url)
