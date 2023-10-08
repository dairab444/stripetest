#! /usr/bin/env python3.6

"""
server.py
Stripe Card Payments Certification.
Python 3.9 or newer required.
"""

import datetime
import json
import os
import time

# TODO: Integrate Stripe
from dotenv import find_dotenv, load_dotenv
from flask import Flask, jsonify, make_response, render_template, request
from flask_cors import CORS, cross_origin

load_dotenv(find_dotenv())


static_dir = str(os.path.abspath(os.path.join(
    __file__, "..", os.getenv("STATIC_DIR"))))
# TODO: Integrate Stripe


frontend = ""
if os.path.isfile("/".join([static_dir, "index.html"])):
    frontend = "vanilla"
else:
    frontend = "react"
    static_dir = str(os.path.abspath(
        os.path.join(__file__, "..", "./templates")))

server_dir = str(os.path.abspath(os.path.join(__file__, "../..")))

app = Flask(
    __name__, static_folder=static_dir, static_url_path="", template_folder=static_dir
)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'X-Requested-With, Content-Type, Accept, Origin, Authorization, access-control-allow-origin'


@app.route("/", methods=["GET"])
def get_main_page():
    # Display checkout page
    if frontend == "vanilla":
        return render_template("index.html")
    else:
        return render_template("react_redirect.html")

# Fetch the Stripe publishable key
#
# Example call:
# curl -X GET http://localhost:4242/config \
#
# Returns: a JSON response of the pubblishable key
#   {
#        key: <STRIPE_PUBLISHABLE_KEY>
#   }


@app.route('/config', methods=['GET'])
def get_stripe_public_key():
    config = {}
    # TODO: Integrate Stripe
    return jsonify(config), 200

# Milestone 1: Signing up
# Shows the lesson sign up page.


@app.route("/lessons", methods=["GET"])
def get_lesson_page():
    # Display lesson signup
    if frontend == "vanilla":
        return render_template("lessons.html")
    else:
        return render_template("react_redirect.html")

# TODO: Integrate Stripe

# Milestone 2: '/schedule-lesson'
# Authorize a payment for a lesson
#
# Parameters:
# customer_id: id of the customer
# amount: amount of the lesson in cents
# description: a description of this lesson
#
# Example call:
# curl --header "Content-Type:application/json" -X POST http://localhost:4242/schedule-lesson
#   -d '{"customer_id": "cus_MbJLR8io8RpVBL", "amount": "4500", "description": "Lesson on Feb 25th"}'
#
# Returns: a JSON response of one of the following forms:
# For a successful payment, return the payment intent:
#   {
#        payment: <payment_intent>
#    }
#
# For errors:
#  {
#    error:
#       code: the code returned from the Stripe error if there was one
#       message: the message returned from the Stripe error. if no payment method was
#         found for that customer return an msg "no payment methods found for <customer_id>"
#    payment_intent_id: if a payment intent was created but not successfully authorized
# }


@app.route("/schedule-lesson", methods=["POST"])
def schdeulelesson():
    # TODO: Integrate Stripe
    pass


# Milestone 2: '/complete-lesson-payment'
# Capture a payment for a lesson.
#
# Parameters:
# amount: (optional) amount to capture if different than the original amount authorized
#
# Example call:
# curl -X POST http://localhost:4242/complete_lesson_payment \
#  -d payment_intent_id=pi_XXX \
#  -d amount=4500
#
# Returns: a JSON response of one of the following forms:
#
# For a successful payment, return the payment intent:
#   {
#        payment: <payment_intent>
#    }
#
# for errors:
#  {
#    error:
#       code: the code returned from the error
#       message: the message returned from the error from Stripe
# }
#
@app.route("/complete-lesson-payment", methods=["POST"])
def complete_lesson_payment():
    # TODO: Integrate Stripe
    pass

# Milestone 2: '/refund-lesson'
# Refunds a lesson payment.  Refund the payment from the customer (or cancel the auth
# if a payment hasn't occurred).
# Sets the refund reason to 'requested_by_customer'
#
# Parameters:
# payment_intent_id: the payment intent to refund
# amount: (optional) amount to refund if different than the original payment
#
# Example call:
# curl -X POST http://localhost:4242/refund-lesson \
#   -d payment_intent_id=pi_XXX \
#   -d amount=2500
#
# Returns
# If the refund is successfully created returns a JSON response of the format:
#
# {
#   refund: refund.id
# }
#
# If there was an error:
#  {
#    error: {
#        code: e.error.code,
#        message: e.error.message
#      }
#  }


@app.route("/refund-lesson", methods=["POST"])
def refund_lesson():
    # TODO: Integrate Stripe
    pass

# Milestone 3: Managing account information
# Displays the account update page for a given customer


@app.route("/account-update/<customer_id>", methods=["GET"])
def get_account_page(customer_id):
    # Display account update page
    if frontend == "vanilla":
        return render_template("account-update.html")
    else:
        return render_template("react_redirect.html")


# Milestone 3: '/delete-account'
# Deletes a customer object if there are no uncaptured payment intents for them.
#
# Parameters:
#   customer_id: the id of the customer to delete
# Changed Example from a POST to a GET. This is bc the -d command is used.
# Example request
#   curl -X POST http://localhost:4242/delete-account \
#    -d customer_id=cusXXX
#
#
# Returns 1 of 3 responses:
# If the customer had no uncaptured charges and was successfully deleted returns the response:
#   {
#        deleted: true
#   }
#
# If the customer had uncaptured payment intents, return a list of the payment intent ids:
#   {
#     uncaptured_payments: ids of any uncaptured payment intents
#   }
#
# If there was an error:
#  {
#    error: {
#        code: e.error.code,
#        message: e.error.message
#      }
#  }
#


@app.route("/delete-account/<customer_id>", methods=["POST"])
def delete_account(customer_id):
    # TODO: Integrate Stripe
    pass


# Milestone 4: '/calculate-lesson-total'
# Returns the total amounts for payments for lessons, ignoring payments
# for videos and concert tickets, ranging over the last 36 hours.
#
# Example call: curl -X GET http://localhost:4242/calculate-lesson-total
#
# Returns a JSON response of the format:
# {
#      payment_total: Total before fees and refunds (including disputes), and excluding payments
#         that haven't yet been captured.
#      fee_total: Total amount in fees that the store has paid to Stripe
#      net_total: Total amount the store has collected from payments, minus their fees.
# }
@app.route("/calculate-lesson-total", methods=["GET"])
def calculate_lesson_total():
    # TODO: Integrate Stripe
    pass


# Milestone 4: '/find-customers-with-failed-payments'
# Returns any customer who meets the following conditions:
# The last attempt to make a payment for that customer failed.
# The payment method associated with that customer is the same payment method used
# for the failed payment, in other words, the customer has not yet supplied a new payment method.
#
# Example request: curl -X GET http://localhost:4242/find-customers-with-failed-payments
#
# Returns a JSON response with information about each customer identified and their associated last payment
# attempt and, info about the payment method on file.
# [
#     {
#         customer: {
#             id: customer.id,
#             email: customer.email,
#             name: customer.name,
#         },
#         payment_intent: {
#             created: created timestamp for the payment intent
#             description: description from the payment intent
#             status: the status of the payment intent
#             error: the error returned from the payment attempt
#         },
#         payment_method: {
#             last4: last four of the card stored on the customer
#             brand: brand of the card stored on the customer
#         }
#     },
#     {},
#     {},
# ]
#
@app.route("/find-customers-with-failed-payments", methods=["GET"])
def find_customers():
    # TODO: Integrate Stripe
    pass


if __name__ == "__main__":
    app.run(host='localhost', port=4242)
