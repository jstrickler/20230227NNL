import sys

print(f"sys.prefix: {sys.prefix}")
print(f"sys.executable: {sys.executable}")
print()
print(f"sys.version: {sys.version}")
print(f"sys.version_info: {sys.version_info}")
print(f"sys.version_info.major: {sys.version_info.major}")
print(f"sys.version_info.minor: {sys.version_info.minor}")
print()
print(f"sys.platform: {sys.platform}")
# win32 -> Windows
# darwin -> Mac
# linux*  -> Linux
print(f"I have a bad feeling about this", file=sys.stderr)

