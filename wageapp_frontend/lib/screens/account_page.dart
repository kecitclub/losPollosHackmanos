import 'package:flutter/material.dart';

class AccountPage extends StatelessWidget {
  final Map<String, String> accountDetails = {
    'Name': 'John Doe',
    'Email': 'johndoe@example.com',
    'Phone': '+1234567890',
    'Address': '123 Main Street, City, Country',
  };

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Account Details'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            ...accountDetails.entries.map((entry) => Padding(
              padding: const EdgeInsets.symmetric(vertical: 8.0),
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    '${entry.key}: ',
                    style: TextStyle(
                      fontWeight: FontWeight.bold,
                      fontSize: 16,
                    ),
                  ),
                  Expanded(
                    child: Text(
                      entry.value,
                      style: TextStyle(fontSize: 16),
                    ),
                  ),
                ],
              ),
            )),
            SizedBox(height: 20),
            Center(
              child: ElevatedButton(
                onPressed: () {
                  // Add logout functionality here
                },
                child: Text('Logout'),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
