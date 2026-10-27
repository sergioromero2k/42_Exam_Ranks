def resolve_dependencies(packages: dict[str, list[str]]) -> list[str]:
    ...


def run_tests(func):
    tests = [
        {
            "name": "Standard Linear Chain",
            "packages": {
                "A": ["B"],
                "B": ["C"],
                "C": []
            },
            "expected": ["C", "B", "A"]
        },
        {
            "name": "Single Node with No Dependencies",
            "packages": {
                "independent": []
            },
            "expected": ["independent"]
        },
        {
            "name": "Deterministic Sorting (Alphabetical Tie-Breaker)",
            "packages": {
                "Z": [],
                "M": [],
                "A": []
            },
            "expected": ["A", "M", "Z"]  # Must sort 0-dependency nodes alphabetically
        },
        {
            "name": "Multiple Dependents (Branching Tree)",
            "packages": {
                "App": ["LibraryX", "LibraryY"],
                "LibraryX": ["Core"],
                "LibraryY": ["Core"],
                "Core": []
            },
            "expected": ["Core", "LibraryX", "LibraryY", "App"] 
            # Note: LibraryX and LibraryY both have in-degree 0 after Core.
            # Alphabetical sorting guarantees X comes before Y.
        },
        {
            "name": "Missing Dependency (Should Skip Affected Packages)",
            "packages": {
                "ValidPackage": [],
                "BrokenPackage": ["GhostDependency"],  # GhostDependency doesn't exist
                "DependentOnBroken": ["BrokenPackage"]
            },
            "expected": ["ValidPackage"] 
            # BrokenPackage is skipped because of GhostDependency.
            # DependentOnBroken is skipped because its prerequisite (BrokenPackage) was filtered out.
        },
        {
            "name": "Simple Direct Cycle (Chicken & Egg)",
            "packages": {
                "chicken": ["egg"],
                "egg": ["chicken"]
            },
            "expected": []
        },
        {
            "name": "Partial Cycle with Valid Sub-Branch (Your Example)",
            "packages": {
                "X": ["A", "Y"],
                "Y": ["X"],
                "A": []
            },
            "expected": []  # Even though 'A' is valid, the overall graph has an unresolvable cycle
        },
        {
            "name": "Longer Circular Loop",
            "packages": {
                "A": ["B"],
                "B": ["C"],
                "C": ["D"],
                "D": ["A"]
            },
            "expected": []
        },
        {
            "name": "Empty Input System",
            "packages": {},
            "expected": []
        }
    ]

    print(f"Running tests for: {func.__name__}\n" + "="*50)
    passed = 0
    for i, t in enumerate(tests, 1):
        result = func(t["packages"])
        if result == t["expected"]:
            print(f"✅ Test {i} Passed: {t['name']}")
            passed += 1
        else:
            print(f"❌ Test {i} FAILED: {t['name']}")
            print(f"   Input:    {t['packages']}")
            print(f"   Expected: {t['expected']}")
            print(f"   Got:      {result}")
        print("-" * 50)

    print(f"\nResult: {passed}/{len(tests)} tests passed.")


if __name__ == "__main__":
    run_tests(resolve_dependencies)