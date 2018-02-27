from main import Main

# SUPER HACK - There are a few errors that will cause the function to error
# but will succeed on a retry, i.e. no verb can be found in proverb, unable to lemmatize verb,
# to hack round this for the moment, we just retry if we fail.

error_count = 0
while error_count < 5:
    try:
        Main('English', 'French').main()
        break
    except Exception as e:
        print(e)
        print(error_count)
        error_count += 1
