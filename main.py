import csv 
import matplotlib.pyplot as plt
import collections 


class OrderProcess:
    def __init__(self):
        self.orders = []

    def load_csv(self, filename):
        try:
            with open(filename, "r") as f:
                reader = csv.reader(f)
                next(reader)  # Пропускаємо заголовок
                for row in reader:
                    try:
                        self.orders.append({
                            "Customer": row[0],
                            "OrderNumber": int(row[1]),
                            "OrderDate": row[2],
                            "OrderAmount": float(row[3]),
                            "Status": row[4]
                        })
                    except ValueError as e:
                        print(f"Error in roow {row} {e}")
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print(f"Error by loading file")

    def save_csv(self, filename):
        try:
            with open(filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Customer", "OrderNumber", "OrderDate", "OrderAmount", "Status"])
                for order in self.orders:
                    writer.writerow([
                        order["Customer"], order["OrderNumber"], order["OrderDate"], order["OrderAmount"], order["Status"]
                    ])
            print("File succes saved.")
        except Exception as e:
            print(f"Error by saving {e}")

    def add_order(self, customer, order_number, order_date, order_amount, status):
        try:
            self.orders.append({
                "Customer": customer,
                "OrderNumber": int(order_number),
                "OrderDate": order_date,
                "OrderAmount": float(order_amount),
                "Status": status
            })
            print("Succefully added")
        except ValueError as e:
            print(f"ERror: {e}")

    def edit_order(self, order_number, customer=None, order_date=None, order_amount=None, status=None):
        for order in self.orders:
            if order["OrderNumber"] == order_number:
                if customer: order["Customer"] = customer
                if order_date: order["OrderDate"] = order_date
                if order_amount is not None: order["OrderAmount"] = float(order_amount)
                if status: order["Status"] = status
                print(f"Order {order_number} succesfluy renewed")
                return True
        print(f"Order {order_number} is not found.")
        return False

    def delete_order(self, order_number):
        for order in self.orders[:]:
            if order["OrderNumber"] == order_number:
                self.orders.remove(order)
                print(f"Order {order_number} succesfully deleted")
                return True
        print(f"Order {order_number} is not found")
        return False

    def display_orders(self):
        print("\List of orders:")
        for order in self.orders:
            print(f"{order['Customer']}, {order['OrderNumber']}, {order['OrderDate']}, {order['OrderAmount']:.2f}, {order['Status']}")
        print()

    def analyze_total(self):
        total_orders = len(self.orders)
        total_amount = sum(order["OrderAmount"] for order in self.orders)
        print(f"Total amount: {total_orders}")
        print(f"Total price: {total_amount:.2f}")
    
    def analyze_status(self):
        status_counts = {"Виконано": 0, "В процесі": 0}
        for order in self.orders:
            if order["Status"].lower() == "виконано":
                status_counts["Виконано"] += 1
            elif order["Status"].lower() == "в процесі":
                status_counts["В процесі"] += 1
        print(f"Виконані замовлення: {status_counts['Виконано']}")
        print(f"Замовлення в процесі: {status_counts['В процесі']}")


    def find_max_order(self):
        if not self.orders:
            print("there are no orders")
            return
        max_order = max(self.orders, key=lambda x: x["OrderAmount"])
        print("Замовлення з найбільшою сумою:")
        print(f"{max_order['Customer']}, {max_order['OrderNumber']}, {max_order['OrderDate']}, {max_order['OrderAmount']:.2f}, {max_order['Status']}")

    def plot_status_pie_chart(self):
        status_counts = {"Виконано": 0, "В процесі": 0}
        for order in self.orders:
            if order["Status"].lower() == "completed":
                status_counts["Виконано"] += 1
            elif order["Status"].lower() == "inprogress":
                status_counts["В процесі"] += 1
        
        labels = ["Виконано", "В процесі"]
        sizes = [status_counts["Виконано"], status_counts["В процесі"]]
        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
        plt.title("Статус замовлень")
        plt.show()

    def plot_orders_histogram(self):  
        dates = [order["OrderDate"] for order in self.orders]
        date_counts = collections.Counter(dates)
        
        plt.figure(figsize=(10, 6))
        plt.bar(date_counts.keys(), date_counts.values())
        plt.xlabel("Дата замовлення")
        plt.ylabel("Кількість замовлень")
        plt.title("Кількість замовлень за датами")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


order_processor = OrderProcess()


order_processor.load_csv("/Users/vlish21/Desktop/module_new/data.csv")


order_processor.display_orders()

order_processor.add_order("Новий клієнт", 101, "2024-11-20", 350.75, "Виконано")


order_processor.edit_order(101, order_amount=400.00, status="В процесі")


order_processor.delete_order(101)


order_processor.analyze_total()


order_processor.analyze_status()


order_processor.find_max_order()


order_processor.plot_status_pie_chart()

# order_processor.plot_orders_histogram()

order_processor.save_csv("updated_orders.csv")

    


