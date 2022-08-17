import sys
import requests
import getopt


# Send slack messages using Slack API

def send_slack_message(message):
    payload = '{"text":"%s"}' % message
    #url = 'https://hooks.slack.com/services/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'
    #url = 'https://hooks.slack.com/services/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'
    response = requests.post(url, data=payload)
    print(response)


def main(message_text):
    message = message_text
    send_slack_message(message)




    #try:
     #   opts, args = getopt.getopt(argv, "hm:", ["message="])

 #   except getopt.GetoptError:
 #       print('Post.py -m <message>')
 #    sys.exit(2)
 #   if len(opts) == 0:
 #       message = 'HELLO WORLD'
 #   for opt, arg in opts:
 #       if opt == '-h':
 #           print('Post.py -m <message>')
 #           sys.exit()
 #       elif opt in ("m-", "--message"):
 #           message = arg
 #   send_slack_message(message)


#if __name__ == "__main__":
 #   main(sys.argv[1:])

#  https: // hooks.slack.com / services / T03PERCQ682 / B03PERLNZM0 / e08g0KnpSKp80qjz90aZ4FqM
