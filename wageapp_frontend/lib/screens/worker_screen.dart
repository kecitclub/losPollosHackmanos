import 'package:flutter/material.dart';
import 'worker_bargain_screen.dart';
import 'account_page.dart';

class WorkerScreen extends StatelessWidget {
  final List<Map<String, String>> customerRequests = [
    {
      'jobTitle': 'Fix Electrical Wiring',
      'description': 'Need help fixing electrical wiring in my house.',
      'budget': '\$100',
    },
    {
      'jobTitle': 'Leaking Pipe Repair',
      'description': 'Urgent plumbing repair for a leaking pipe.',
      'budget': '\$80',
    },
    {
      'jobTitle': 'Furniture Assembly',
      'description': 'Need help assembling a wooden table and chairs.',
      'budget': '\$60',
    },
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Customer Requests'),
      ),
      body: ListView.builder(
        itemCount: customerRequests.length,
        itemBuilder: (context, index) {
          final request = customerRequests[index];
          return Card(
            margin: EdgeInsets.symmetric(vertical: 8.0, horizontal: 16.0),
            child: ListTile(
              title: Text(request['jobTitle']!),
              subtitle: Text(request['description']!),
              trailing: Text(request['budget']!),
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => WorkerBargainScreen(request: request),
                  ),
                );
              },
            ),
          );
        },
      ),
      bottomNavigationBar: BottomNavigationBar(
        items: const [
          BottomNavigationBarItem(
            icon: Icon(Icons.history),
            label: 'History',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.account_circle),
            label: 'Account',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.notifications),
            label: 'Notifications',
          ),
        ],
        onTap: (index) {
          if (index == 0) {
            // Navigate to History Screen (to be implemented)
          } else if (index == 1) {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => AccountPage()),
            );
          } else if (index == 2) {
            // Navigate to Notifications Screen (to be implemented)
          }
        },
      ),
    );
  }
}
