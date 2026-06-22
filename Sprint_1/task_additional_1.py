types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

# Удаление дублей из списков с тикетами
def remove_duplicates(ticket_list, used_tickets):
    unique_tickets = []

    for ticket in ticket_list:
        if ticket not in used_tickets:
            unique_tickets.append(ticket)
            used_tickets.append(ticket)

    return unique_tickets


def create_tickets_by_type(types, tickets):
    result = {}
    used_tickets = []

    for priority in types:
        unique_tickets = remove_duplicates(tickets[priority],used_tickets)
        result[types[priority]] = unique_tickets

    return result

tickets_by_type = create_tickets_by_type(types, tickets)

for bug_type, ticket_list in tickets_by_type.items():
    print(bug_type, ':', ticket_list)