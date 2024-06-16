name: CI

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-20.04

    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Set up Node.js 20
        uses: actions/setup-node@v2
        with:
          node-version: '20'

      - name: Get Date
        id: get-date
        run: |
          echo "date=$(date -u "+%Y%m%d")" >> $GITHUB_ENV
        shell: bash

      - name: Cache Buildozer global directory
        uses: actions/cache@v2
        with:
          path: .buildozer_global
          key: buildozer-global-${{ hashFiles('buildozer.spec') }}

      - name: Cache Buildozer
        uses: actions/cache@v2
        with:
          path: .buildozer
          key: ${{ runner.os }}-${{ steps.get-date.outputs.date }}-${{ hashFiles('buildozer.spec') }}

      - name: Build with Buildozer
        uses: ArtemSBulgakov/buildozer-action@v1
        with:
          command: buildozer android debug
          buildozer_version: stable

      - name: Upload artifacts
        uses: actions/upload-artifact@v2
        with:
          name: package
          path: ${{ steps.buildozer.outputs.filename }}
