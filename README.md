# Python Pickle Deserialization Vulnerability Demo

This project is a simple demonstration of how a Remote Code Execution (RCE) vulnerability can occur during deserialization when using Python’s built-in `pickle` module.

## Description

Python’s `pickle` module is a powerful tool for serializing and deserializing Python objects. However, if you deserialize pickle data from an untrusted or unverified source, it can pose a serious security threat.

This demo shows how loading a maliciously crafted pickle file can result in executing arbitrary system commands — in this case, launching the calculator application on the system.

* **`mal_gen.py`**: Generates a `malicious.pkl` file that contains a payload to launch the calculator.
* **`pkl_load.py`**: Loads `malicious.pkl` and triggers the vulnerability.

## How to Run

1. **Generate a Malicious Pickle File:**

   ```bash
   python mal_gen.py
   ```

   This command will create a file named `malicious.pkl`.

2. **Demonstrate the Vulnerability:**

   ```bash
   python pkl_load.py
   ```

   When you run this script, `pickle.load()` will execute the payload and launch the calculator (depending on your operating system).

## Security Warning

⚠️ **Never deserialize pickle files from untrusted or unverified sources.**

A malicious attacker can craft a pickle file that executes arbitrary code on your system, potentially leading to data theft, system compromise, or further attacks.

## Detection

You can scan pickle files for potentially dangerous payloads using tools like [picklescan](https://github.com/Paradoxis/Scavenger). For example:

```bash
pip install picklescan
picklescan -p ./malicious.pkl
```

Sample output:

```
/path/to/malicious.pkl: dangerous import 'nt system' FOUND
----------- SCAN SUMMARY -----------
Scanned files: 1
Infected files: 1
Dangerous globals: 1
```

### Additional Detection Tips

* **Static Analysis:** Look for suspicious imports (`os`, `sys`, `subprocess`) in custom pickle reducers.
* **Content Inspection:** Use hex editors or tools to inspect the raw pickle bytecode for suspicious opcodes like `GLOBAL` and `REDUCE`.
* **Runtime Monitoring:** Monitor file loading paths and alert on unexpected system calls during `pickle.load()`.
* **Safe Alternatives:** Use `pickletools.dis` to disassemble pickle data for manual inspection.

## Disclaimer

*This project is intended for educational purposes only.*
