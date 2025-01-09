// main.dart
import 'package:flutter/material.dart';
import 'screens/homepage.dart';
import 'screens/worker_screen.dart';
import 'screens/customer_screen.dart';
import 'screens/worker_list_screen.dart';
import 'screens/bargain_screen.dart';
import 'screens/account_page.dart';

void main() {
  runApp(WorkerHiringApp());
}

class WorkerHiringApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Worker Hiring App',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: HomePage(),
      routes: {
        '/workerList': (context) => WorkerListScreen(workerType: 'Default'),
        '/bargain': (context) => BargainScreen(workerName: 'Default Worker'),
        '/account': (context) => AccountPage(),
      },
    );
  }
}
