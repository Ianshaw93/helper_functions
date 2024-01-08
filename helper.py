paid_product_blurb = "if you want our expert support to apply automation principles outlined in the ebook give us a shout! We have 4 slots left for 1to1 coaching sessions left. Use the code 'FITMATE25' for 25% off the standard price. 7 day money back guarantee!"

business_info = "Fitmate automating insta dm's for fitness professionals"
paid_product_info = '''1to1 coaching sessions x5 1 hour each on how to setup insta automations for inbound messages.
Normally £500 now 25% off
7 day money back guarantee
Only 4 spaces left
'''



def extract_ebook_blurb(paid_product_blurb):
    start_of_apply = paid_product_blurb.index('apply')
    end_of_apply = start_of_apply + len('apply')

    start_of_principles = paid_product_blurb.index('principles')

    filtered = paid_product_blurb[end_of_apply:start_of_principles]
    return filtered




if __name__ == "__main__":
    print(extract_ebook_blurb(paid_product_blurb))