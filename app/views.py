from flask import Blueprint, request, jsonify
from . import supabase

views_bp = Blueprint('views', __name__)

""" API Routes for Calendar + Events """

@views_bp.route('/calendar', methods=['GET'])
def get_events():
    token = request.headers.get('Authorization').split(" ")[1]
    # Validate the token and retrieve the user's information
    user_response = supabase.auth.get_user(token)

    if user_response.user.aud == 'authenticated':
        user_id = user_response.user.id

        # Fetch the events for this user
        response = supabase.table('Events').select('*').eq('user_id', user_id).execute()
        data = response.data

        return jsonify(data), 200
    else:
        return jsonify({'message': 'Unauthorized'}), 401
    
@views_bp.route('/calendar', methods=['POST'])
def create_event():
    token = request.headers.get('Authorization').split(" ")[1]
    user_response = supabase.auth.get_user(token)

    if user_response.user.aud == 'authenticated':
        user_id = user_response.user.id

        # Get the event details from the request body
        event_details = request.json

        # Create the new event for this user
        response = supabase.table('Events').insert({**event_details, 'user_id': user_id}).execute()
        data = response.data

        return jsonify(data), 201
    else:
        return jsonify({'message': 'Unauthorized'}), 401
    
@views_bp.route('/calendar/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    token = request.headers.get('Authorization').split(" ")[1]
    user_response = supabase.auth.get_user(token)

    if user_response.user.aud == 'authenticated':
        user_id = user_response.user.id

        # Get the updated event details from the request body
        updated_details = request.json

        # Update the event
        response = supabase.table('Events').update(updated_details).eq('id', event_id).eq('user_id', user_id).execute()
        data = response.data

        return jsonify(data), 200
    else:
        return jsonify({'message': 'Unauthorized'}), 401
    
@views_bp.route('/calendar/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    token = request.headers.get('Authorization').split(" ")[1]
    user_response = supabase.auth.get_user(token)

    if user_response.user.aud == 'authenticated':
        user_id = user_response.user.id

        # Delete the event
        response = supabase.table('Events').delete().eq('id', event_id).eq('user_id', user_id).execute()

        return jsonify({'message': 'Event deleted'}), 200
    else:
        return jsonify({'message': 'Unauthorized'}), 401

""" API Routes for To-do + Reminders """

@views_bp.route('/todo', methods=['GET'])
def get_reminders():
    token = request.headers.get('Authorization').split(" ")[1]

    user_response = supabase.auth.get_user(token)

    if user_response.user.aud == 'authenticated':
        user_id = user_response.user.id

        # Fetch the reminders for this user
        response = supabase.table('Reminders').select('*').eq('user_id', user_id).execute()
        data = response.data

        return jsonify(data), 200
    else:
        return jsonify({'message': 'Unauthorized'}), 401
    
@views_bp.route('/todo', methods=['POST'])
def create_reminder():
    token = request.headers.get('Authorization').split(" ")[1]
    user_response = supabase.auth.get_user(token)

    if user_response.user.aud == 'authenticated':
        user_id = user_response.user.id

        # Get the reminder details from the request body
        reminder_details = request.json

        # Create the new reminder for this user
        response = supabase.table('Reminders').insert({**reminder_details, 'user_id': user_id}).execute()
        data = response.data

        return jsonify(data), 201
    else:
        return jsonify({'message': 'Unauthorized'}), 401

@views_bp.route('/todo/<int:reminder_id>', methods=['PUT'])
def update_reminder(reminder_id):
    token = request.headers.get('Authorization').split(" ")[1]
    user_response = supabase.auth.get_user(token)

    if user_response.user.aud == 'authenticated':
        user_id = user_response.user.id
        updated_details = request.json

        # Update the reminder
        response = supabase.table('Reminders').update(updated_details).eq('id', reminder_id).eq('user_id', user_id).execute()
        data = response.data

        return jsonify(data), 200
    else:
        return jsonify({'message': 'Unauthorized'}), 401

@views_bp.route('/todo/<int:reminder_id>', methods=['DELETE'])
def delete_reminder(reminder_id):
    token = request.headers.get('Authorization').split(" ")[1]
    user_response = supabase.auth.get_user(token)

    if user_response.user.aud == 'authenticated':
        user_id = user_response.user.id

        # Delete the reminder
        response = supabase.table('Reminders').delete().eq('id', reminder_id).eq('user_id', user_id).execute()

        return jsonify({'message': 'Reminder deleted'}), 200
    else:
        return jsonify({'message': 'Unauthorized'}), 401
