import 'package:flutter/material.dart';
import 'bargain_screen.dart';

class WorkerListScreen extends StatelessWidget {
  final String workerType;

  WorkerListScreen({required this.workerType});

  final List<Map<String, String>> workers = [
    {'name': 'John Doe', 'distance': '2 km'},
    {'name': 'Jane Smith', 'distance': '3 km'},
    {'name': 'Mike Johnson', 'distance': '1.5 km'},
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('$workerType Workers Nearby'),
      ),
      body: ListView.builder(
        itemCount: workers.length,
        itemBuilder: (context, index) {
          final worker = workers[index];
          return ListTile(
            title: Text(worker['name']!),
            subtitle: Text('Distance: ${worker['distance']}'),
            trailing: ElevatedButton(
              child: Text('Bargain'),
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => BargainScreen(workerName: worker['name']!),
                  ),
                );
              },
            ),
          );
        },
      ),
    );
  }
}