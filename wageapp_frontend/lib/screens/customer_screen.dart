import 'package:flutter/material.dart';
import 'worker_list_screen.dart';
import 'account_page.dart'; // Import the AccountPage

class CustomerScreen extends StatelessWidget {
  final List<Map<String, String>> workerTypes = [
    {'type': 'Electrician', 'icon': 'https://via.placeholder.com/50'},
    {'type': 'Plumber', 'icon': 'https://via.placeholder.com/50'},
    {'type': 'Carpenter', 'icon': 'https://via.placeholder.com/50'},
    {'type': 'Painter', 'icon': 'https://via.placeholder.com/50'},
    {'type': 'Mechanic', 'icon': 'https://via.placeholder.com/50'},
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Select Worker Type'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: GridView.builder(
          gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
            crossAxisCount: 2,
            crossAxisSpacing: 16.0,
            mainAxisSpacing: 16.0,
          ),
          itemCount: workerTypes.length,
          itemBuilder: (context, index) {
            final worker = workerTypes[index];
            return GestureDetector(
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => WorkerListScreen(workerType: worker['type']!),
                  ),
                );
              },
              child: Container(
                decoration: BoxDecoration(
                  color: Colors.blue,
                  borderRadius: BorderRadius.circular(12.0),
                ),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Image.network(
                      worker['icon']!,
                      height: 50,
                      width: 50,
                    ),
                    SizedBox(height: 10),
                    Text(
                      worker['type']!,
                      style: TextStyle(
                        color: Colors.white,
                        fontSize: 16,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ],
                ),
              ),
            );
          },
        ),
      ),
      bottomNavigationBar: BottomNavigationBar(
        items: [
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
          switch (index) {
            case 0:
            // Navigate to History screen (to be implemented)
              break;
            case 1:
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => AccountPage()),
              );
              break;
            case 2:
            // Navigate to Notifications screen (to be implemented)
              break;
          }
        },
      ),
    );
  }
}
