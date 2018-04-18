# randomduk-py
Python wrapper for random-d.uk

### Installation:

Put randomduk.py somewhere in your project folder and import it in your code

### Example:

```python
#import required files
import randomduk

duk = randomduk.Randomduk()

random = duk.random_no_async()

print(random.url, random.message)
```

### Functions:
```python
# Return random duck image (Async)
await random() #optionally random(type='gif') or random(type='jpg')
# Return random duck image(Non-Async)
random_no_async() #optionally random(type='gif') or random(type='jpg')
# Get specific duck image
getimg(number)
# Get specific duck gif
getgif(number)
# Get HTTP duck
httpduck(number)
# Upload a file to the queue for adding to the site (Async)
upload(file) # Requires filename to be passed
# Upload a file to the queue for adding to the site (Non-Async)
upload_no_async(file) # Requires filename to be passed
```

### Exceptions: 
```python
CouldNotGetDuckError(status_code)
CouldNotUploadError(status_code, error_message)
```


