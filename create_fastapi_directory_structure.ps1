# Name of the base project folder
$projectName = "course_enrollment"

# List of folders to create
$folders = @(
    "$projectName/app/api/v1/endpoints",
    "$projectName/app/models",
    "$projectName/app/schemas",
    "$projectName/app/services",
    "$projectName/app/db",
    "$projectName/app/core",
    "$projectName/app/utils",
    "$projectName/tests"
)

# Create folders
foreach ($folder in $folders) {
    New-Item -ItemType Directory -Force -Path $folder
}

# Create common starter files
New-Item -ItemType File -Path "$projectName/app/main.py"
New-Item -ItemType File -Path "$projectName/requirements.txt"
New-Item -ItemType File -Path "$projectName/.env"
New-Item -ItemType File -Path "$projectName/README.md"

# Create __init__.py files for Python modules
$initPaths = @(
    "$projectName/app/__init__.py",
    "$projectName/app/api/__init__.py",
    "$projectName/app/api/v1/__init__.py",
    "$projectName/app/api/v1/endpoints/__init__.py",
    "$projectName/app/models/__init__.py",
    "$projectName/app/schemas/__init__.py",
    "$projectName/app/services/__init__.py",
    "$projectName/app/db/__init__.py",
    "$projectName/app/core/__init__.py",
    "$projectName/app/utils/__init__.py",
    "$projectName/tests/__init__.py"
)

foreach ($init in $initPaths) {
    New-Item -ItemType File -Path $init
}

Write-Output "✅ FastAPI project structure created successfully!"
