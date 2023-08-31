import facebookads

# Create an ad account object.
ad_account = facebookads.AdAccount('YOUR_AD_ACCOUNT_ID')

# Create a request object.
request = facebookads.AdSetsRequest(
    account_id=ad_account.id,
    targeting_spec={
        'interests': ['travel']
    }
)

# Make the request.
response = ad_account.get_ad_sets(request)

# Print the results.
for ad_set in response['data']:
    print(ad_set['id'], ad_set['name'], ad_set['targeting']['interests'])
