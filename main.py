import time

from logger import Logger


logger = Logger()
logger.remove_oldlog()


def main():
    logger.info('sample log')

    sample_array = [1, 2, 3, 4, 5]
    logger.info(sample_array)

    time.sleep(1)

    sample_dict = {
            'key1': 'value1',
            'key2': 1e10,
            'sub_key3': [1, 2, 3, 4, 5],
        }
    logger.info(sample_dict)

    print(5 / 0)  # エラーを発生させる


if __name__ == '__main__':
    try:
        logger.info('##### Bigin #####')
        main()

    except Exception as e:
        logger.error(e)

    finally:
        logger.info('###### End ######')
