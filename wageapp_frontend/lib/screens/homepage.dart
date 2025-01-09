import 'package:flutter/material.dart';
import 'customer_screen.dart';
import 'worker_screen.dart';

class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  bool isCustomerMode = true; // Toggle between Customer and Worker

  void toggleMode() {
    setState(() {
      isCustomerMode = !isCustomerMode;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(isCustomerMode ? 'Customer Mode' : 'Worker Mode'),
        actions: [
          Switch(
            value: isCustomerMode,
            onChanged: (value) => toggleMode(),
            activeColor: Colors.green,
            inactiveThumbColor: Colors.red,
          ),
        ],
      ),
      body: isCustomerMode ? CustomerScreen() : WorkerScreen(),
    );
  }
}
