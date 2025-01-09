import 'package:flutter/material.dart';

class WorkerBargainScreen extends StatelessWidget {
  final Map<String, String> request;

  const WorkerBargainScreen({Key? key, required this.request}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Bargain with Customer'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Text(
              'Job Title: ${request['jobTitle']}',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 8),
            Text('Description: ${request['description']}'),
            SizedBox(height: 8),
            Text('Customer Budget: ${request['budget']}'),
            SizedBox(height: 16),
            TextField(
              decoration: InputDecoration(
                labelText: 'Your Offer',
                border: OutlineInputBorder(),
              ),
              keyboardType: TextInputType.number,
            ),
            SizedBox(height: 16),
            ElevatedButton(
              onPressed: () {
                // Submit offer logic
              },
              child: Text('Submit Offer'),
            ),
          ],
        ),
      ),
    );
  }
}