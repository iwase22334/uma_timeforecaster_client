# uma_timeforecaster

## Install
```
pip3 install .
```

## class DummyRace
* vote_tansyo(id, vote_list)
  * id: race id
  ```
    [ 'year', 'monthday', 'jyocd', 'kaiji', 'nichiji', 'racenum']
  ```
  * result: list of tuple 
    ```
    {
        "race_id": {
            "year": "2018",
            "monthday":"1001",
            "jyocd":"01",
            "kaiji":"01",
            "nichiji": "01",
            "racenum": "01"
        },

        "bins": 150
        "width": 0.3
        "dataset": [
            { 
                "umaban": "03",
                "name": "シタヤマゴーゴー",
                "pdf": [
                    {x:64.1,y:0.00},
                    {x:64.2,y:0.06},
                    {x:64.3,y:0.011},
                    ...
                    {x:78.8,y:0.00},
                    ]
            },
            ...
        ]

    }
    ```
